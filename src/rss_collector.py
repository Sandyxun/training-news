"""
RSS采集器 - 从各个培训行业网站采集最新资讯
"""

import feedparser
import json
import os
from datetime import datetime, timedelta
from config import RSS_SOURCES, NEWS_FILE, DATA_DIR
import hashlib


class RSSCollector:
    def __init__(self):
        self.sources = RSS_SOURCES
        self.news_data = []

    def fetch_rss(self, url, source_name, category):
        """
        获取单个RSS源的内容
        """
        try:
            print(f"正在采集: {source_name}...")
            feed = feedparser.parse(url)

            if feed.bozo:
                print(f"警告: {source_name} RSS解析可能有问题")

            articles = []
            # 获取最近7天的文章（临时测试）
            week_ago = datetime.now() - timedelta(days=7)

            for entry in feed.entries[:10]:  # 只取最新10条
                try:
                    # 解析发布时间
                    published = None
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        published = datetime(*entry.published_parsed[:6])
                    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                        published = datetime(*entry.updated_parsed[:6])

                    # 生成唯一ID
                    article_id = hashlib.md5(
                        f"{entry.link}".encode('utf-8')
                    ).hexdigest()

                    article = {
                        'id': article_id,
                        'title': entry.title,
                        'link': entry.link,
                        'summary': entry.get('summary', '')[:300],  # 限制摘要长度
                        'published': published.isoformat() if published else datetime.now().isoformat(),
                        'source': source_name,
                        'category': category,
                    }

                    # 只添加最近7天的文章（临时测试）
                    if published and published >= week_ago:
                        articles.append(article)
                    elif not published:  # 如果没有时间，也添加
                        articles.append(article)

                except Exception as e:
                    print(f"处理文章时出错: {str(e)}")
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
    print("\n最新资讯预览:")
    for i, article in enumerate(articles[:3], 1):
        print(f"\n{i}. {article['title']}")
        print(f"   来源: {article['source']} | 分类: {article['category']}")
        print(f"   链接: {article['link']}")
