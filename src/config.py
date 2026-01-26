"""
配置文件 - 企业人才发展资讯推送系统
"""

# RSSHub服务器地址（可选，如果官方实例不可用，可以自建或使用其他镜像）
RSSHUB_BASE_URL = 'https://rsshub.app'  # RSSHub官方实例

# RSS源配置 - 企业人才发展相关
RSS_SOURCES = [
    # === 国际源 ===
    {
        'name': 'ATD (人才发展协会)',
        'url': 'https://www.td.org/rss-feeds/td-at-work',
        'category': '人才发展',
        'description': '全球最大的人才发展协会'
    },
    {
        'name': 'Chief Learning Officer',
        'url': 'https://www.chieflearningofficer.com/feed/',
        'category': '企业学习',
        'description': '面向企业首席学习官的专业资讯'
    },
    {
        'name': 'Training Industry',
        'url': 'https://trainingindustry.com/feed/',
        'category': '培训产业',
        'description': '企业培训与人才发展行业资讯'
    },
    {
        'name': 'eLearning Industry',
        'url': 'https://elearningindustry.com/feed',
        'category': '企业学习',
        'description': '企业在线学习平台与技术'
    },
    {
        'name': 'HR Dive - Learning',
        'url': 'https://www.hrdive.com/feeds/news/',
        'category': 'HR与学习',
        'description': '人力资源与员工发展新闻'
    },

    # === 中文微信公众号源（通过RSSHub） ===
    # 使用说明：需要替换{biz}参数为实际的公众号ID
    # 获取方法见 WECHAT_RSSHUB_GUIDE.md

    # 示例配置（需要替换实际的biz参数）：
    # {
    #     'name': '培训经理指南',
    #     'url': f'{RSSHUB_BASE_URL}/wechat/mp/homepage/MzAwNDQ0MDk3Mg==',
    #     'category': '培训管理',
    #     'description': '培训经理的实战指南'
    # },
    # {
    #     'name': '培训江湖',
    #     'url': f'{RSSHUB_BASE_URL}/wechat/mp/homepage/公众号BIZ参数',
    #     'category': '培训行业',
    #     'description': '培训行业资讯与观点'
    # },

    # === 其他中文源 ===
    # 可以添加有RSS的中文网站
]

# 微信公众号配置（待添加biz参数）
# 填写你想订阅的公众号名称，稍后使用工具获取biz参数
WECHAT_ACCOUNTS = [
    '培训经理指南',
    '培训江湖',
    '培训杂志',
    'ATD中国',
    # 可以继续添加其他公众号
]

# 邮件配置（使用环境变量，不要直接写在代码里）
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': '',  # 从环境变量读取
    'sender_password': '',  # 从环境变量读取
    'receiver_email': '',  # 从环境变量读取
}

# 时区设置
TIMEZONE = 'Asia/Shanghai'

# 网页配置
WEBSITE_TITLE = '企业人才发展每日资讯'
WEBSITE_DESCRIPTION = '每天早上9点更新，汇聚企业人才发展、组织学习、培训管理最新动态'

# 数据文件路径
DATA_DIR = 'data'
DOCS_DIR = 'docs'
NEWS_FILE = f'{DATA_DIR}/news.json'
