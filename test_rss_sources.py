#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""测试所有RSS源的可用性"""

import feedparser
import sys
import os

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from config import RSS_SOURCES

def test_rss_source(source):
    """测试单个RSS源"""
    name = source['name']
    url = source['url']

    try:
        print(f'\n正在测试: {name}')
        print(f'  URL: {url}')

        feed = feedparser.parse(url)

        if not feed.entries:
            print(f'  [FAIL] 无法获取文章')
            return False

        print(f'  [OK] 成功! 获取到 {len(feed.entries)} 篇文章')
        if feed.entries:
            print(f'  最新: {feed.entries[0].title[:60]}')
        return True

    except Exception as e:
        print(f'  [ERROR] 错误: {str(e)}')
        return False

def main():
    print('=' * 70)
    print('RSS源可用性测试')
    print('=' * 70)

    success_count = 0
    fail_count = 0

    for source in RSS_SOURCES:
        if test_rss_source(source):
            success_count += 1
        else:
            fail_count += 1

    print('\n' + '=' * 70)
    print(f'测试完成!')
    print(f'  成功: {success_count}')
    print(f'  失败: {fail_count}')
    print(f'  总计: {len(RSS_SOURCES)}')
    print('=' * 70)

if __name__ == '__main__':
    main()
