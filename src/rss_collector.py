 """
  RSS采集器 - 优化版本
  """

  import feedparser
  import json
  import os
  from datetime import datetime, timedelta
  from config import RSS_SOURCES, NEWS_FILE, DATA_DIR
  import hashlib
  import time


  class RSSCollector:
      def __init__(self):
          self.sources = RSS_SOURCES
          self.news_data = []

      def fetch_rss(self, url, source_name, category, timeout=15):
          """
          获取单个RSS源的内容（优化版）
          """
          try:
              print(f"正在采集: {source_name}...")

              # 添加User-Agent避免被拦截
              feed = feedparser.parse(url, request_headers={
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
              })

              # 检查HTTP状态
              if hasattr(feed, 'status'):
                  print(f"  HTTP状态: {feed.status}")
                  if feed.status >= 400:
                      print(f"✗ {source_name}: HTTP错误 {feed.status}")
                      return []

              if feed.bozo:
                  print(f"  警告: RSS解析有问题 - {feed.bozo_exception}")
                  # 即使有警告也继续尝试，因为有些feed虽然有小问题但仍可用

              if not feed.entries:
                  print(f"✗ {source_name}: 没有找到文章")
                  return []

              articles = []
              # 放宽时间限制：改为最近30天
              month_ago = datetime.now() - timedelta(days=30)

              for entry in feed.entries[:20]:  # 增加到20条
                  try:
                      # 解析发布时间（更宽松）
                      published = None
                      if hasattr(entry, 'published_parsed') and entry.published_parsed:
                          try:
                              published = datetime(*entry.published_parsed[:6])
                          except:
                              pass
                      elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                          try:
                              published = datetime(*entry.updated_parsed[:6])
                          except:
                              pass

                      # 如果没有时间，使用当前时间
                      if not published:
                          published = datetime.now()

                      # 生成唯一ID
                      article_id = hashlib.md5(
                          f"{entry.link}".encode('utf-8')
                      ).hexdigest()

                      # 获取摘要
                      summary = ''
                      if hasattr(entry, 'summary'):
                          summary = entry.summary
                      elif hasattr(entry, 'description'):
                          summary = entry.description

                      # 清理HTML标签
                      import re
                      summary = re.sub(r'<[^>]+>', '', summary)
                      summary = summary.strip()[:300]

                      article = {
                          'id': article_id,
                          'title': entry.title,
                          'link': entry.link,
                          'summary': summary,
                          'published': published.isoformat(),
                          'source': source_name,
                          'category': category,
                      }

                      # 只过滤30天前的文章
                      if published >= month_ago:
                          articles.append(article)

                  except Exception as e:
                      print(f"  处理文章时出错: {str(e)}")
                      continue

              print(f"✓ {source_name}: 采集到 {len(articles)} 篇文章")
              return articles

          except Exception as e:
              print(f"✗ {source_name} 采集失败: {str(e)}")
              return []

      def collect_all(self):
          """
          采集所有RSS源
          """
          print("=" * 50)
          print("开始采集RSS源...")
          print("=" * 50)

          all_articles = []
          for source in self.sources:
              articles = self.fetch_rss(
                  source['url'],
                  source['name'],
                  source['category']
              )
              all_articles.extend(articles)
              time.sleep(1)  # 添加延迟避免被限流

          # 去重（根据ID）
          unique_articles = {}
          for article in all_articles:
              if article['id'] not in unique_articles:
                  unique_articles[article['id']] = article

          self.news_data = sorted(
              unique_articles.values(),
              key=lambda x: x['published'],
              reverse=True
          )

          print("=" * 50)
          print(f"采集完成！共获取 {len(self.news_data)} 篇不重复的文章")
          print("=" * 50)

          return self.news_data

      def save_to_file(self):
          """
          保存到JSON文件
          """
          os.makedirs(DATA_DIR, exist_ok=True)

          data = {
              'update_time': datetime.now().isoformat(),
              'total': len(self.news_data),
              'articles': self.news_data
          }

          with open(NEWS_FILE, 'w', encoding='utf-8') as f:
              json.dump(data, f, ensure_ascii=False, indent=2)

          print(f"数据已保存到: {NEWS_FILE}")


  if __name__ == '__main__':
      collector = RSSCollector()
      articles = collector.collect_all()
      collector.save_to_file()

      # 打印前3条作为示例
      if articles:
          print("\n最新资讯预览:")
          for i, article in enumerate(articles[:3], 1):
              print(f"\n{i}. {article['title']}")
              print(f"   来源: {article['source']} | 分类: {article['category']}")
              print(f"   链接: {article['link']}")
      else:
          print("\n⚠️ 未采集到任何文章，请检查RSS源配置")
