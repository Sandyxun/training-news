#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试新的邮件格式（带分类导航）
"""

import sys
import os

sys.path.insert(0, 'src')
from email_sender import EmailSender

# 创建发送器
sender = EmailSender()

# 加载数据
news_data = sender.load_news_data()

if news_data:
    # 生成HTML
    html_content = sender.generate_html_email(news_data)

    # 保存为文件
    output_file = 'email_preview_categorized.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"[OK] 邮件预览已生成: {output_file}")
    print(f"[OK] 文件路径: {os.path.abspath(output_file)}")

    # 统计
    articles = news_data.get('articles', [])
    print(f"\n[INFO] 总文章数: {len(articles)}")

    # 按新分类统计
    category_map = {
        '企业学习': '人才发展',
        '人才发展': '人才发展',
        '人力资源': '人才发展',
        '管理': '人才发展',
        '培训产业': '人才发展',
        '商学院': '人才发展',
        'AI': 'AI技术',
        '技术': 'AI技术',
        '科技商业': '科技商业',
    }

    new_categories = {}
    for article in articles:
        orig_cat = article['category']
        new_cat = category_map.get(orig_cat, '科技商业')
        new_categories[new_cat] = new_categories.get(new_cat, 0) + 1

    print("\n[INFO] 分类统计:")
    for cat, count in sorted(new_categories.items()):
        print(f"  {cat}: {count}篇")

    # 尝试在浏览器中打开
    try:
        import webbrowser
        webbrowser.open(f'file://{os.path.abspath(output_file)}')
        print("\n[OK] 已在浏览器中打开预览")
    except:
        print("\n[INFO] 请手动在浏览器中打开预览文件")
else:
    print("[ERROR] 无法加载数据")
