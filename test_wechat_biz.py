#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试微信公众号 biz 参数"""

import feedparser

biz = 'MjM5MzU3NTk4Mw=='
url = f'https://rsshub.app/wechat/mp/homepage/{biz}'

print(f'Testing: {url}')
print('=' * 60)

try:
    feed = feedparser.parse(url)

    if feed.bozo:
        print('Warning: RSS parsing might have issues')

    if not feed.entries:
        print('WARNING: RSS accessible but no articles found')
        print('Possible reasons:')
        print('  1. Incorrect biz parameter')
        print('  2. Account has no articles')
        print('  3. RSSHub instance issue')
    else:
        print(f'SUCCESS! Found {len(feed.entries)} articles')
        print(f'Account title: {feed.feed.get("title", "Unknown")}')
        print(f'Account description: {feed.feed.get("description", "Unknown")}')
        print()
        print('Latest 5 articles:')
        print('-' * 60)
        for i, entry in enumerate(feed.entries[:5], 1):
            print(f'{i}. {entry.title}')
            print(f'   Published: {entry.get("published", "Unknown")}')
            print(f'   Link: {entry.link}')
            print()

        print('\nConfiguration to add to config.py:')
        print('-' * 60)
        print(f"""
    {{
        'name': '{feed.feed.get("title", "公众号名称")}',
        'url': '{url}',
        'category': '培训行业',
        'description': '{feed.feed.get("description", "描述")[:50]}'
    }},
        """)

except Exception as e:
    print(f'ERROR: Test failed - {str(e)}')
    import traceback
    traceback.print_exc()
