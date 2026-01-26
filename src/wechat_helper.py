"""
微信公众号RSS配置工具
帮助获取和测试公众号的RSS地址
"""

import feedparser
import sys


def test_rsshub_url(biz, rsshub_base='https://rsshub.app'):
    """
    测试RSSHub URL是否可用
    """
    url = f'{rsshub_base}/wechat/mp/homepage/{biz}'
    print(f"\n正在测试: {url}")
    print("=" * 60)

    try:
        feed = feedparser.parse(url)

        if feed.bozo:
            print("❌ RSS解析失败")
            print(f"错误: {feed.bozo_exception}")
            return False

        if not feed.entries:
            print("⚠️  RSS可以访问，但没有文章")
            print("可能原因：")
            print("  1. biz参数不正确")
            print("  2. 该公众号暂无文章")
            print("  3. RSSHub实例问题")
            return False

        print(f"✅ 成功！找到 {len(feed.entries)} 篇文章\n")
        print(f"公众号标题: {feed.feed.get('title', '未知')}")
        print(f"公众号描述: {feed.feed.get('description', '未知')}\n")

        print("最新5篇文章:")
        print("-" * 60)
        for i, entry in enumerate(feed.entries[:5], 1):
            print(f"{i}. {entry.title}")
            print(f"   发布时间: {entry.get('published', '未知')}")
            print(f"   链接: {entry.link}\n")

        print("\n✅ 配置可用！可以添加到 config.py")
        print("\n添加以下配置到 RSS_SOURCES:")
        print("-" * 60)
        print(f"""
    {{
        'name': '{feed.feed.get('title', '公众号名称')}',
        'url': '{url}',
        'category': '培训行业',  # 根据实际情况修改
        'description': '{feed.feed.get('description', '描述')[:50]}'
    }},
        """)

        return True

    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")
        return False


def extract_biz_from_url(url):
    """
    从微信文章URL中提取biz参数
    """
    if '__biz=' in url:
        biz = url.split('__biz=')[1].split('&')[0]
        return biz
    return None


def main():
    print("=" * 60)
    print("微信公众号RSS配置工具")
    print("=" * 60)

    print("\n选择操作：")
    print("1. 测试已知的biz参数")
    print("2. 从文章URL提取biz参数")
    print("3. 批量测试多个biz")

    choice = input("\n请选择 (1/2/3): ").strip()

    if choice == '1':
        biz = input("\n请输入biz参数: ").strip()
        rsshub = input("RSSHub地址 (直接回车使用默认 https://rsshub.app): ").strip()
        if not rsshub:
            rsshub = 'https://rsshub.app'

        test_rsshub_url(biz, rsshub)

    elif choice == '2':
        url = input("\n请粘贴微信文章URL: ").strip()
        biz = extract_biz_from_url(url)

        if biz:
            print(f"\n✅ 提取到的biz参数: {biz}")

            test = input("\n是否测试该biz? (y/n): ").strip().lower()
            if test == 'y':
                rsshub = input("RSSHub地址 (直接回车使用默认): ").strip()
                if not rsshub:
                    rsshub = 'https://rsshub.app'
                test_rsshub_url(biz, rsshub)
        else:
            print("\n❌ 无法从URL中提取biz参数")
            print("请确保URL包含 __biz= 参数")

    elif choice == '3':
        print("\n请输入多个biz参数（每行一个），输入空行结束:")
        biz_list = []
        while True:
            biz = input().strip()
            if not biz:
                break
            biz_list.append(biz)

        rsshub = input("\nRSSHub地址 (直接回车使用默认): ").strip()
        if not rsshub:
            rsshub = 'https://rsshub.app'

        print(f"\n开始测试 {len(biz_list)} 个公众号...")
        success_count = 0
        for biz in biz_list:
            if test_rsshub_url(biz, rsshub):
                success_count += 1
            print("\n" + "=" * 60 + "\n")

        print(f"\n测试完成！成功: {success_count}/{len(biz_list)}")

    else:
        print("无效选择")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n已取消")
        sys.exit(0)
