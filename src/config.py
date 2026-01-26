"""
配置文件 - 企业人才发展资讯推送系统
"""

# RSSHub服务器地址（可选，如果官方实例不可用，可以自建或使用其他镜像）
RSSHUB_BASE_URL = 'https://rsshub.app'  # RSSHub官方实例

# RSS源配置 - 企业人才发展相关（中英文混合）
RSS_SOURCES = [
    # === 中文源（优先） ===
    {
        'name': '36氪-企业服务',
        'url': 'https://rsshub.app/36kr/news/latest',
        'category': '企业资讯',
        'description': '企业服务与管理相关新闻'
    },
    {
        'name': '人人都是产品经理-职场',
        'url': 'https://rsshub.app/woshipm/popular',
        'category': '职场管理',
        'description': '职场与管理热门文章'
    },
    {
        'name': '虎嗅-商业',
        'url': 'https://rsshub.app/huxiu/article',
        'category': '商业管理',
        'description': '商业与管理深度文章'
    },

    # === 精选国际源（提供国际视野） ===
    {
        'name': 'ATD (人才发展协会)',
        'url': 'https://www.td.org/rss-feeds/td-at-work',
        'category': '人才发展',
        'description': '全球最大的人才发展协会'
    },
    {
        'name': 'Training Industry',
        'url': 'https://trainingindustry.com/feed/',
        'category': '培训产业',
        'description': '企业培训与人才发展行业资讯'
    },

    # === 想添加微信公众号？ ===
    # 参考 WECHAT_RSSHUB_GUIDE.md 文档
    # 或使用 src/wechat_helper.py 工具测试

    # 示例：培训经理指南（需要替换实际的biz参数）
    # {
    #     'name': '培训经理指南',
    #     'url': 'https://rsshub.app/wechat/mp/homepage/你的biz参数',
    #     'category': '培训管理',
    #     'description': '培训经理的实战指南'
    # },
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
