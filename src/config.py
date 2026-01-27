"""
配置文件 - 企业人才发展资讯推送系统
"""

# RSSHub服务器地址（可选，如果官方实例不可用，可以自建或使用其他镜像）
RSSHUB_BASE_URL = 'https://rsshub.app'  # RSSHub官方实例

# RSS源配置 - 中英文混合，聚焦企业人才发展
RSS_SOURCES = [
    # === 中文源（直接RSS） ===
    {
        'name': 'FT中文网-管理',
        'url': 'https://www.ftchinese.com/rss/management',
        'category': '管理',
        'description': '金融时报中文网-管理专题'
    },
    {
        'name': 'FT中文网-商学院',
        'url': 'https://www.ftchinese.com/rss/mba',
        'category': '商学院',
        'description': '金融时报中文网-MBA与商学院'
    },

    # === 专业人才发展源（英文） ===
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
        'description': '企业培训与人才发展专业资讯'
    },
    {
        'name': 'Chief Learning Officer',
        'url': 'https://www.chieflearningofficer.com/feed/',
        'category': '企业学习',
        'description': '首席学习官的专业内容'
    },
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
