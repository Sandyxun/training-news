#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试多个 RSSHub 实例"""

import feedparser

biz = 'MjM5MzU3NTk4Mw=='

# 多个 RSSHub 实例
rsshub_instances = [
    'https://rsshub.app',
    'https://rsshub.rssforever.com',
    'https://rss.shab.fun',
    'https://rsshub.ktachibana.party',
]

print(f'Testing biz: {biz}')
print('=' * 60)

for instance in rsshub_instances:
    url = f'{instance}/wechat/mp/homepage/{biz}'
    print(f'\nTrying: {instance}')
    print('-' * 60)

    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            print(f'  No articles found')
        else:
            print(f'  SUCCESS! Found {len(feed.entries)} articles')
            print(f'  Title: {feed.feed.get("title", "Unknown")}')
            print(f'  Description: {feed.feed.get("description", "")[:80]}')
            print(f'\n  Latest 3 articles:')
            for i, entry in enumerate(feed.entries[:3], 1):
                print(f'    {i}. {entry.title[:60]}')

            print(f'\n  ✓ This instance works! Use this URL:')
            print(f'    {url}')
            break

    except Exception as e:
        print(f'  Error: {str(e)}')

print('\n' + '=' * 60)
