 """
  配置文件 - 企业人才发展资讯推送系统
  """

  # RSSHub服务器地址
  RSSHUB_BASE_URL = 'https://rsshub.app'

  # RSS源配置
RSS_SOURCES = [
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
      {
          'name': 'Harvard Business Review',
          'url': 'https://feeds.hbr.org/harvardbusiness',
          'category': '管理',
          'description': '哈佛商业评论'
      },
  ]

  # 微信公众号配置
  WECHAT_ACCOUNTS = [
      '培训经理指南',
      '培训江湖',
      '培训杂志',
      'ATD中国',
  ]

  # 邮件配置
  EMAIL_CONFIG = {
      'smtp_server': 'smtp.gmail.com',
      'smtp_port': 587,
      'sender_email': '',
      'sender_password': '',
      'receiver_email': '',
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
