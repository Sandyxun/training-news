"""
配置文件 - 企业人才发展资讯推送系统
"""

# RSSHub服务器地址（可选，如果官方实例不可用，可以自建或使用其他镜像）
RSSHUB_BASE_URL = 'https://rsshub.app'  # RSSHub官方实例

# RSS源配置 - 中文为主，聚焦企业人才发展和AI
RSS_SOURCES = [
    # === 科技商业媒体（中文）- 可用 ===
    {
        'name': '36氪',
        'url': 'https://36kr.com/feed',
        'category': '科技商业',
        'description': '科技创业媒体，关注创新与商业'
    },
    {
        'name': '虎嗅网',
        'url': 'https://www.huxiu.com/rss/0.xml',
        'category': '科技商业',
        'description': '科技财经媒体，深度商业分析'
    },
    {
        'name': '钛媒体',
        'url': 'https://www.tmtpost.com/rss.xml',
        'category': '科技商业',
        'description': '科技第一媒体，关注技术与商业变革'
    },

    # === AI 人工智能专题（中文）- 可用 ===
    {
        'name': '机器之心',
        'url': 'https://www.jiqizhixin.com/rss',
        'category': 'AI',
        'description': '专业的人工智能媒体和产业服务平台'
    },
    {
        'name': '量子位',
        'url': 'https://www.qbitai.com/feed',
        'category': 'AI',
        'description': '人工智能内容平台，专注AI技术和应用'
    },

    # === 技术媒体（中文）- 可用 ===
    {
        'name': 'InfoQ中文',
        'url': 'https://www.infoq.cn/feed',
        'category': '技术',
        'description': '软件开发与技术领导力'
    },

    # === 企业学习和人才发展（英文）- 可用 ===
    {
        'name': 'Chief Learning Officer',
        'url': 'https://www.chieflearningofficer.com/feed/',
        'category': '企业学习',
        'description': '首席学习官的专业内容'
    },

    # === AI 资讯（英文）- 可用 ===
    {
        'name': 'MIT Technology Review - AI',
        'url': 'https://www.technologyreview.com/topic/artificial-intelligence/feed/',
        'category': 'AI',
        'description': 'MIT科技评论AI频道'
    },
    {
        'name': 'OpenAI Blog',
        'url': 'https://openai.com/blog/rss.xml',
        'category': 'AI',
        'description': 'OpenAI官方博客'
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
WEBSITE_TITLE = '企业人才发展与AI资讯'
WEBSITE_DESCRIPTION = '每天更新，汇聚企业人才发展、组织学习、培训管理与人工智能最新动态'

# 数据文件路径
DATA_DIR = 'data'
DOCS_DIR = 'docs'
NEWS_FILE = f'{DATA_DIR}/news.json'
