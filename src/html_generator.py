"""
HTML生成器 - 生成GitHub Pages网站
"""

import json
import os
from datetime import datetime
from config import NEWS_FILE, DOCS_DIR, WEBSITE_TITLE, WEBSITE_DESCRIPTION


class HTMLGenerator:
    def __init__(self):
        self.docs_dir = DOCS_DIR

    def load_news_data(self):
        """加载新闻数据"""
        try:
            with open(NEWS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"加载数据失败: {str(e)}")
            return None

    def generate_index_html(self, news_data):
        """生成首页HTML"""
        articles = news_data.get('articles', [])
        total = news_data.get('total', 0)
        update_time = datetime.fromisoformat(news_data.get('update_time', datetime.now().isoformat()))

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{WEBSITE_DESCRIPTION}">
    <title>{WEBSITE_TITLE}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>📚 {WEBSITE_TITLE}</h1>
            <p>{WEBSITE_DESCRIPTION}</p>
        </header>

        <div class="stats">
            <div class="stat-item">
                <span class="stat-number">{total}</span>
                <span class="stat-label">今日资讯</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{len(articles)}</span>
                <span class="stat-label">文章总数</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">最后更新</span>
                <span class="stat-time">{update_time.strftime('%Y-%m-%d %H:%M')}</span>
            </div>
        </div>

        <main class="articles">
"""

        if articles:
            for i, article in enumerate(articles, 1):
                published = datetime.fromisoformat(article['published'])
                html += f"""
            <article class="article-card">
                <div class="article-header">
                    <span class="article-number">{i}</span>
                    <span class="category-tag">{article['category']}</span>
                </div>
                <h2 class="article-title">
                    <a href="{article['link']}" target="_blank" rel="noopener">{article['title']}</a>
                </h2>
                <div class="article-meta">
                    <span class="source">📰 {article['source']}</span>
                    <span class="time">🕐 {published.strftime('%m月%d日 %H:%M')}</span>
                </div>
                <p class="article-summary">{article['summary']}</p>
                <a href="{article['link']}" class="read-more" target="_blank" rel="noopener">阅读全文 →</a>
            </article>
"""
        else:
            html += """
            <div class="no-content">
                <p>📭 今天暂无新资讯</p>
            </div>
"""

        html += """
        </main>

        <footer class="footer">
            <p>🤖 本网站由 GitHub Actions 自动生成并更新</p>
            <p>数据来源: RSS订阅 | 每天早上9点自动更新</p>
            <p><a href="https://github.com/yourusername/training-news" target="_blank">查看源代码</a></p>
        </footer>
    </div>

    <script>
        // 添加动画效果
        document.addEventListener('DOMContentLoaded', function() {
            const articles = document.querySelectorAll('.article-card');
            articles.forEach((article, index) => {
                article.style.animationDelay = `${index * 0.1}s`;
            });
        });
    </script>
</body>
</html>
"""
        return html

    def generate_css(self):
        """生成CSS样式"""
        css = """/* 培训行业资讯网站样式 */

:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --text-color: #2c3e50;
    --text-light: #7f8c8d;
    --bg-color: #f5f7fa;
    --card-bg: #ffffff;
    --border-radius: 12px;
    --shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    --shadow-hover: 0 8px 12px rgba(0, 0, 0, 0.12);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background: var(--bg-color);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* 头部 */
.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    padding: 60px 40px;
    border-radius: var(--border-radius);
    text-align: center;
    margin-bottom: 30px;
    box-shadow: var(--shadow);
}

.header h1 {
    font-size: 2.5rem;
    margin-bottom: 10px;
    font-weight: 700;
}

.header p {
    font-size: 1.1rem;
    opacity: 0.95;
}

/* 统计区域 */
.stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.stat-item {
    background: var(--card-bg);
    padding: 25px;
    border-radius: var(--border-radius);
    text-align: center;
    box-shadow: var(--shadow);
    transition: transform 0.3s ease;
}

.stat-item:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-hover);
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--primary-color);
    margin-bottom: 5px;
}

.stat-label {
    display: block;
    color: var(--text-light);
    font-size: 0.95rem;
}

.stat-time {
    display: block;
    font-size: 1rem;
    color: var(--text-color);
    margin-top: 5px;
}

/* 文章列表 */
.articles {
    display: grid;
    gap: 20px;
}

.article-card {
    background: var(--card-bg);
    padding: 30px;
    border-radius: var(--border-radius);
    border-left: 4px solid var(--primary-color);
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
    opacity: 0;
    animation: fadeInUp 0.6s ease forwards;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.article-card:hover {
    transform: translateX(5px);
    box-shadow: var(--shadow-hover);
}

.article-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 15px;
}

.article-number {
    display: inline-block;
    width: 32px;
    height: 32px;
    line-height: 32px;
    text-align: center;
    background: var(--primary-color);
    color: white;
    border-radius: 50%;
    font-weight: 600;
    font-size: 0.9rem;
}

.category-tag {
    display: inline-block;
    padding: 4px 12px;
    background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    color: white;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}

.article-title {
    font-size: 1.4rem;
    margin-bottom: 12px;
    line-height: 1.4;
}

.article-title a {
    color: var(--text-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

.article-title a:hover {
    color: var(--primary-color);
}

.article-meta {
    display: flex;
    gap: 20px;
    margin-bottom: 15px;
    color: var(--text-light);
    font-size: 0.9rem;
}

.article-summary {
    color: #555;
    line-height: 1.8;
    margin-bottom: 15px;
}

.read-more {
    display: inline-block;
    color: var(--primary-color);
    text-decoration: none;
    font-weight: 600;
    transition: transform 0.3s ease;
}

.read-more:hover {
    transform: translateX(5px);
}

/* 无内容提示 */
.no-content {
    background: var(--card-bg);
    padding: 60px;
    text-align: center;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow);
}

.no-content p {
    font-size: 1.2rem;
    color: var(--text-light);
}

/* 页脚 */
.footer {
    margin-top: 60px;
    padding: 30px;
    text-align: center;
    color: var(--text-light);
    font-size: 0.9rem;
}

.footer p {
    margin: 5px 0;
}

.footer a {
    color: var(--primary-color);
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .container {
        padding: 15px;
    }

    .header {
        padding: 40px 20px;
    }

    .header h1 {
        font-size: 1.8rem;
    }

    .article-card {
        padding: 20px;
    }

    .article-title {
        font-size: 1.2rem;
    }

    .stats {
        grid-template-columns: 1fr;
    }
}
"""
        return css

    def generate_all(self):
        """生成所有网页文件"""
        os.makedirs(self.docs_dir, exist_ok=True)

        # 加载数据
        news_data = self.load_news_data()
        if not news_data:
            print("错误: 无法生成网页，数据加载失败")
            return False

        try:
            # 生成index.html
            index_html = self.generate_index_html(news_data)
            with open(f'{self.docs_dir}/index.html', 'w', encoding='utf-8') as f:
                f.write(index_html)
            print(f"[OK] 生成首页: {self.docs_dir}/index.html")

            # 生成style.css
            css = self.generate_css()
            with open(f'{self.docs_dir}/style.css', 'w', encoding='utf-8') as f:
                f.write(css)
            print(f"[OK] 生成样式: {self.docs_dir}/style.css")

            return True

        except Exception as e:
            print(f"[FAIL] 生成网页失败: {str(e)}")
            return False


if __name__ == '__main__':
    generator = HTMLGenerator()
    generator.generate_all()
