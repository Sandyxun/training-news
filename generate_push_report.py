#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
临时推送脚本 - 生成推送报告
"""

import json
import os
import webbrowser
from datetime import datetime

def generate_push_report():
    """生成临时推送报告"""

    # 读取数据
    try:
        with open('data/news.json', 'r', encoding='utf-8') as f:
            news_data = json.load(f)
    except Exception as e:
        print(f"错误: 无法读取数据文件 - {str(e)}")
        return False

    articles = news_data.get('articles', [])
    total = news_data.get('total', 0)
    update_time = news_data.get('update_time', '')

    # 按分类统计
    category_stats = {}
    for article in articles:
        cat = article['category']
        category_stats[cat] = category_stats.get(cat, 0) + 1

    # 生成推送报告
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>今日资讯推送 - {datetime.now().strftime('%Y-%m-%d')}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .container {{
            background: white;
            border-radius: 15px;
            padding: 40px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 30px;
            border-bottom: 3px solid #667eea;
        }}
        .header h1 {{
            color: #2c3e50;
            margin: 0 0 10px 0;
            font-size: 2.5rem;
        }}
        .header .date {{
            color: #7f8c8d;
            font-size: 1.2rem;
        }}
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .stat-card .number {{
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .stat-card .label {{
            font-size: 0.9rem;
            opacity: 0.9;
        }}
        .category-section {{
            margin-bottom: 40px;
        }}
        .category-title {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            font-size: 1.5rem;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .article {{
            background: #f8f9fa;
            padding: 25px;
            margin-bottom: 15px;
            border-radius: 10px;
            border-left: 5px solid #667eea;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .article:hover {{
            transform: translateX(5px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        .article-title {{
            font-size: 1.3rem;
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .article-title a {{
            color: #2c3e50;
            text-decoration: none;
        }}
        .article-title a:hover {{
            color: #667eea;
        }}
        .article-meta {{
            color: #7f8c8d;
            font-size: 0.9rem;
            margin-bottom: 12px;
        }}
        .article-summary {{
            color: #555;
            line-height: 1.8;
        }}
        .footer {{
            text-align: center;
            margin-top: 50px;
            padding-top: 30px;
            border-top: 2px solid #e0e0e0;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 企业人才发展与AI资讯推送</h1>
            <div class="date">{datetime.now().strftime('%Y年%m月%d日')}</div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="number">{total}</div>
                <div class="label">今日资讯</div>
            </div>
"""

    # 添加分类统计
    for cat, count in sorted(category_stats.items(), key=lambda x: x[1], reverse=True):
        html += f"""
            <div class="stat-card">
                <div class="number">{count}</div>
                <div class="label">{cat}</div>
            </div>
"""

    html += """
        </div>
"""

    # 按分类组织文章
    categories = {}
    for article in articles:
        cat = article['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(article)

    # 输出各分类的文章
    for cat in sorted(categories.keys(), key=lambda x: len(categories[x]), reverse=True):
        html += f"""
        <div class="category-section">
            <div class="category-title">
                <span>{cat}</span>
                <span>{len(categories[cat])} 篇</span>
            </div>
"""

        for i, article in enumerate(categories[cat], 1):
            pub_time = datetime.fromisoformat(article['published'])
            html += f"""
            <div class="article">
                <div class="article-title">
                    {i}. <a href="{article['link']}" target="_blank">{article['title']}</a>
                </div>
                <div class="article-meta">
                    📰 {article['source']} · 🕐 {pub_time.strftime('%m月%d日 %H:%M')}
                </div>
                <div class="article-summary">{article['summary']}</div>
            </div>
"""

        html += """
        </div>
"""

    html += f"""
        <div class="footer">
            <p>🤖 本报告由 RSS 采集系统自动生成</p>
            <p>更新时间: {datetime.fromisoformat(update_time).strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>
"""

    # 保存报告
    report_file = f'push_report_{datetime.now().strftime("%Y%m%d")}.html'
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[OK] 推送报告已生成: {report_file}")
        print(f"[OK] 文件路径: {os.path.abspath(report_file)}")

        # 尝试在浏览器中打开
        try:
            webbrowser.open(f'file://{os.path.abspath(report_file)}')
            print("[OK] 已在浏览器中打开报告")
        except:
            print("[INFO] 请手动在浏览器中打开报告文件")

        return True
    except Exception as e:
        print(f"[FAIL] 生成报告失败: {str(e)}")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("临时推送报告生成器")
    print("=" * 60)
    generate_push_report()
    print("=" * 60)
