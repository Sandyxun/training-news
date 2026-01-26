# 企业人才发展每日资讯 📚

> 每天早上9点自动推送企业人才发展、组织学习、培训管理最新资讯到你的邮箱

完全免费，基于 GitHub Actions + RSS + 邮件推送实现

---

## ✨ 功能特点

- 🆓 **完全免费** - 使用GitHub免费服务，无需任何费用
- ⏰ **定时推送** - 每天早上9点（北京时间）自动运行
- 📧 **邮件通知** - 资讯直达邮箱，不错过任何重要信息
- 🌐 **网页查看** - 通过GitHub Pages网站查看历史资讯
- 🔄 **自动更新** - 无需人工干预，全自动运行

## 📊 数据来源

聚合以下优质RSS源：

**国际源：**
- **ATD (人才发展协会)** - 全球最大的人才发展专业组织
- **Chief Learning Officer** - 面向企业首席学习官的专业资讯
- **Training Industry** - 企业培训与人才发展行业动态
- **eLearning Industry** - 企业在线学习平台与技术
- **HR Dive** - 人力资源与员工发展新闻

**中文公众号源（可选配置）：**
- **培训经理指南** - 培训经理的实战指南
- **培训江湖** - 培训行业资讯与观点
- **培训杂志** - 培训行业专业期刊
- **ATD中国** - ATD在中国的官方账号
- 更多公众号可自行添加...

> 📖 公众号订阅需要额外配置，详见 [WECHAT_RSSHUB_GUIDE.md](WECHAT_RSSHUB_GUIDE.md)

## 🚀 快速开始

### 1. Fork本仓库

点击右上角的 `Fork` 按钮，将仓库复制到你的GitHub账户

### 2. 配置邮件服务

需要配置3个GitHub Secrets（在仓库 Settings → Secrets and variables → Actions）：

#### 如果使用Gmail：

1. **开启两步验证** - 前往 [Google账户安全设置](https://myaccount.google.com/security)
2. **生成应用专用密码**：
   - 访问 [应用专用密码](https://myaccount.google.com/apppasswords)
   - 选择"邮件"和"其他设备"
   - 生成16位密码（记住这个密码）

3. **添加Secrets**：
   ```
   SENDER_EMAIL = 你的Gmail地址（如 your@gmail.com）
   EMAIL_PASSWORD = 刚才生成的16位应用专用密码
   RECEIVER_EMAIL = 接收邮件的地址（可以和发送邮箱相同）
   ```

#### 如果使用QQ邮箱：

1. 开启SMTP服务 - 前往 QQ邮箱设置 → 账户 → 开启POP3/SMTP服务
2. 获取授权码（16位字符）
3. 修改 `src/config.py` 中的SMTP配置：
   ```python
   EMAIL_CONFIG = {
       'smtp_server': 'smtp.qq.com',
       'smtp_port': 587,
       ...
   }
   ```

### 3. 启用GitHub Actions

1. 进入仓库的 `Actions` 标签页
2. 点击 `I understand my workflows, go ahead and enable them`
3. 启用工作流

### 4. 配置GitHub Pages

1. 进入 Settings → Pages
2. Source 选择 `Deploy from a branch`
3. Branch 选择 `gh-pages` 分支，目录选择 `/ (root)`
4. 保存后，你的网站将发布在 `https://你的用户名.github.io/training-news`

### 5. 手动测试运行

第一次可以手动触发测试：

1. 进入 `Actions` 标签页
2. 点击左侧 `企业人才发展资讯每日推送` 工作流
3. 点击 `Run workflow` → `Run workflow`
4. 等待几分钟，查看运行结果

## 📁 项目结构

```
training-news/
├── .github/workflows/
│   └── daily_news.yml        # GitHub Actions定时任务配置
├── src/
│   ├── config.py             # 配置文件（RSS源、邮件设置等）
│   ├── rss_collector.py      # RSS采集脚本
│   ├── email_sender.py       # 邮件发送模块
│   ├── html_generator.py     # 网页生成器
│   └── wechat_helper.py      # 微信公众号配置辅助工具
├── data/
│   └── news.json             # 采集的资讯数据
├── docs/                     # GitHub Pages网站目录
│   ├── index.html
│   └── style.css
├── requirements.txt          # Python依赖
├── README.md                 # 项目说明
├── DEPLOYMENT.md             # 详细部署指南
└── WECHAT_RSSHUB_GUIDE.md    # 微信公众号订阅指南
```

## ⚙️ 自定义配置

### 订阅微信公众号

如果想订阅"培训经理指南"、"培训江湖"等微信公众号：

1. 阅读 [WECHAT_RSSHUB_GUIDE.md](WECHAT_RSSHUB_GUIDE.md) 获取详细步骤
2. 使用 `src/wechat_helper.py` 工具测试公众号配置
3. 将配置添加到 `src/config.py` 的 `RSS_SOURCES`

**快速测试工具：**
```bash
cd src
python wechat_helper.py
```

### 修改推送时间

编辑 `.github/workflows/daily_news.yml`，修改 cron 表达式：

```yaml
schedule:
  - cron: '0 1 * * *'  # UTC时间1点 = 北京时间9点
```

在线工具: [Crontab Guru](https://crontab.guru/)

### 添加更多RSS源

编辑 `src/config.py`，在 `RSS_SOURCES` 列表中添加：

```python
{
    'name': '网站名称',
    'url': 'RSS订阅地址',
    'category': '分类标签',
    'description': '简短描述'
}
```

### 修改网站标题和描述

编辑 `src/config.py`：

```python
WEBSITE_TITLE = '你的网站标题'
WEBSITE_DESCRIPTION = '你的网站描述'
```

## 🔍 常见问题

### Q: 邮件发送失败？

A: 检查以下几点：
1. Secrets配置是否正确
2. Gmail需要使用应用专用密码，不是账户密码
3. 如果使用QQ邮箱，需要修改SMTP配置
4. 查看Actions运行日志获取详细错误信息

### Q: 为什么收不到邮件？

A:
1. 检查垃圾邮件文件夹
2. 确认RECEIVER_EMAIL配置正确
3. 查看Actions运行日志，确认邮件已发送

### Q: 如何添加中文RSS源？

A: 很多中文网站没有提供RSS源，你可以：
1. 检查网站是否有RSS图标
2. 使用RSSHub等服务生成RSS源
3. 或者后续改用爬虫方式获取

### Q: 能否推送到微信？

A: 可以！修改 `src/email_sender.py`，使用以下服务：
- Server酱（免费）
- 企业微信机器人（免费）
- Telegram Bot（免费）

### Q: GitHub Actions免费额度够用吗？

A: 完全够用！
- 公开仓库：无限制
- 私有仓库：每月2000分钟
- 本项目每次运行约2-3分钟，每月最多消耗90分钟

## 📝 许可证

MIT License - 自由使用、修改和分发

## 🤝 贡献

欢迎提交Issue和Pull Request！

如果觉得有用，请给个⭐️Star支持一下！

---

**注意**: 本项目仅供学习交流使用，请遵守各网站的使用条款和robots协议。
