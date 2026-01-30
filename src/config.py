"""
配置文件 - 企业人才发展资讯推送系统
"""

# RSSHub服务器地址（可选，如果官方实例不可用，可以自建或使用其他镜像）
RSSHUB_BASE_URL = 'https://rsshub.app'  # RSSHub官方实例

# RSS源配置 - 中英文混合，聚焦企业人才发展
RSS_SOURCES = [
      # === 可靠的中文源 ===
      {
          'name': '36氪-企业服务',
          'url': 'https://36kr.com/feed/enterprise',
          'category': '企业服务',
          'description': '36氪企业服务频道'
      },
      {
          'name': '虎嗅-商业',
          'url': 'https://www.huxiu.com/rss/0.xml',
          'category': '商业',
          'description': '虎嗅商业资讯'
      },
      {
          'name': '人人都是产品经理',
          'url': 'http://www.woshipm.com/feed',
          'category': '产品管理',
          'description': '产品与运营'
      },

      # === 使用RSSHub聚合微信公众号 ===
      {
          'name': '培训杂志',
          'url': 'https://rsshub.app/wechat/mp/homepage/MzA5MDc1ODQ0MA==',
          'category': '培训行业',
          'description': '培训杂志公众号'
      },

      # === 备用英文源（如果可以访问） ===
      {
          'name': 'Harvard Business Review',
          'url': 'https://feeds.hbr.org/harvardbusiness',
          'category': '管理',
          'description': '哈佛商业评论'
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
