"""
  配置文件 - 企业人才发展资讯推送系统
  """

  RSSHUB_BASE_URL = 'https://rsshub.app'

RSS_SOURCES = [
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

  WECHAT_ACCOUNTS = [
      '培训经理指南',
      '培训江湖',
      '培训杂志',
      'ATD中国',
  ]

  EMAIL_CONFIG = {
      'smtp_server': 'smtp.gmail.com',
      'smtp_port': 587,
      'sender_email': '',
      'sender_password': '',
      'receiver_email': '',
  }

  TIMEZONE = 'Asia/Shanghai'

  WEBSITE_TITLE = '企业人才发展每日资讯'
  WEBSITE_DESCRIPTION = '每天早上9点更新，汇聚企业人才发展、组织学习、培训管理最新动态'

  DATA_DIR = 'data'
  DOCS_DIR = 'docs'
  NEWS_FILE = f'{DATA_DIR}/news.json'
