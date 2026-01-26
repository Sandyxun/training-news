# 企业人才发展每日资讯 - 部署指南

## 📋 部署步骤详解

### 第一步：准备GitHub仓库

1. **注册GitHub账号**
   - 访问 https://github.com
   - 如果没有账号，点击 Sign up 注册

2. **创建新仓库**
   - 点击右上角 "+" → "New repository"
   - Repository name: `training-news`（或其他名称）
   - 选择 "Public"（公开仓库免费使用GitHub Pages）
   - 不要勾选 "Initialize this repository with a README"
   - 点击 "Create repository"

3. **上传项目代码**

   **方式一：使用Git命令行**（推荐）
   ```bash
   cd D:\projects\training-news
   git init
   git add .
   git commit -m "初始化项目"
   git branch -M main
   git remote add origin https://github.com/你的用户名/training-news.git
   git push -u origin main
   ```

   **方式二：使用GitHub Desktop**
   - 下载并安装 [GitHub Desktop](https://desktop.github.com/)
   - File → Add Local Repository → 选择项目文件夹
   - Publish repository

   **方式三：手动上传**
   - 在GitHub仓库页面点击 "uploading an existing file"
   - 拖拽所有文件上传

---

### 第二步：配置Gmail邮箱

#### 1. 开启Gmail两步验证

1. 访问 https://myaccount.google.com/security
2. 找到"两步验证"，点击开启
3. 按照提示完成验证（手机号码验证）

#### 2. 生成应用专用密码

1. 访问 https://myaccount.google.com/apppasswords
2. 选择应用：选择"邮件"
3. 选择设备：选择"其他（自定义名称）"，输入"GitHub Actions"
4. 点击"生成"
5. **记下生成的16位密码**（格式如：abcd efgh ijkl mnop）

> **注意**：不是你的Gmail密码，而是刚才生成的16位应用专用密码！

---

### 第三步：配置GitHub Secrets

1. 进入你的GitHub仓库页面
2. 点击 `Settings`（设置）标签
3. 左侧菜单找到 `Secrets and variables` → `Actions`
4. 点击 `New repository secret` 按钮

添加以下3个Secrets：

| Name | Value | 说明 |
|------|-------|------|
| `SENDER_EMAIL` | your@gmail.com | 发送邮件的Gmail地址 |
| `EMAIL_PASSWORD` | abcdefghijklmnop | 刚才生成的16位应用专用密码（去掉空格） |
| `RECEIVER_EMAIL` | your@gmail.com | 接收邮件的地址（可以相同）|

**添加方法**：
- Name填写: `SENDER_EMAIL`
- Secret填写: `your@gmail.com`
- 点击 "Add secret"
- 重复以上步骤添加另外两个

---

### 第四步：启用GitHub Actions

1. 进入仓库的 `Actions` 标签页
2. 如果看到提示："Workflows aren't being run on this forked repository"
3. 点击绿色按钮 `I understand my workflows, go ahead and enable them`

---

### 第五步：配置GitHub Pages

1. 进入 `Settings` → 左侧菜单找到 `Pages`
2. **Source** 部分：
   - 选择 `Deploy from a branch`
3. **Branch** 部分：
   - Branch: 选择 `gh-pages`（第一次运行后会自动创建）
   - Folder: 选择 `/ (root)`
4. 点击 `Save`

> **提示**：首次需要先运行一次工作流，才会创建 `gh-pages` 分支

---

### 第六步：首次运行测试

#### 手动触发工作流

1. 进入 `Actions` 标签页
2. 左侧选择 `企业人才发展资讯每日推送` 工作流
3. 点击右侧 `Run workflow` 按钮
4. 点击绿色的 `Run workflow` 确认
5. 等待1-3分钟

#### 查看运行结果

- 绿色✅ = 成功
- 红色❌ = 失败（点击进去查看日志）

#### 检查邮件

- 查看你的邮箱（包括垃圾邮件文件夹）
- 应该收到一封标题为"📚 企业人才发展每日资讯"的邮件

#### 查看网站

- 访问: `https://你的用户名.github.io/training-news`
- 应该能看到生成的资讯网页

---

## 🔧 常见问题排查

### 问题1：邮件发送失败

**错误信息**: `Authentication failed` 或 `Username and Password not accepted`

**解决方法**:
1. 确认使用的是应用专用密码，不是Gmail账户密码
2. 确认应用专用密码复制时没有包含空格
3. 确认已开启两步验证
4. 尝试重新生成应用专用密码

### 问题2：GitHub Actions运行失败

**查看错误日志**:
1. Actions页面 → 点击失败的运行
2. 点击左侧的job
3. 展开每个步骤查看详细日志

**常见原因**:
- Secrets配置错误或未配置
- RSS源无法访问（网络问题）
- Python依赖安装失败

### 问题3：GitHub Pages显示404

**解决方法**:
1. 确认已经运行过一次工作流
2. 确认 `gh-pages` 分支已创建
3. 在Settings → Pages中重新保存配置
4. 等待几分钟，GitHub Pages需要部署时间

### 问题4：收不到邮件

**检查清单**:
- [ ] 查看垃圾邮件文件夹
- [ ] 确认RECEIVER_EMAIL配置正确
- [ ] 查看Actions日志，确认邮件发送成功
- [ ] 尝试换一个接收邮箱测试

### 问题5：RSS采集失败

**可能原因**:
- RSS源网站暂时无法访问
- RSS格式变化
- 网络限制

**解决方法**:
- 查看Actions日志，看哪个源失败
- 在 `src/config.py` 中注释掉问题源
- 或更换其他RSS源

---

## 🎯 使用QQ邮箱替代Gmail

如果你无法使用Gmail，可以用QQ邮箱：

### 1. 开启QQ邮箱SMTP服务

1. 登录QQ邮箱网页版
2. 设置 → 账户
3. 找到"POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务"
4. 开启"POP3/SMTP服务"
5. 点击"生成授权码"，按照提示操作
6. **保存生成的授权码**（16位字符）

### 2. 修改代码配置

编辑 `src/config.py` 文件：

```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.qq.com',  # 改为QQ邮箱
    'smtp_port': 587,
    'sender_email': '',
    'sender_password': '',
    'receiver_email': '',
}
```

### 3. 配置GitHub Secrets

- `SENDER_EMAIL`: 你的QQ邮箱（如 123456@qq.com）
- `EMAIL_PASSWORD`: 刚才生成的授权码
- `RECEIVER_EMAIL`: 接收邮箱

---

## ⏰ 修改推送时间

编辑 `.github/workflows/daily_news.yml`：

```yaml
schedule:
  - cron: '0 1 * * *'  # UTC时间1点 = 北京时间9点
```

**常用时间对照表**（北京时间 → UTC时间）：

| 北京时间 | UTC时间 | cron表达式 |
|---------|---------|-----------|
| 07:00 | 23:00 | `0 23 * * *` |
| 08:00 | 00:00 | `0 0 * * *` |
| 09:00 | 01:00 | `0 1 * * *` |
| 12:00 | 04:00 | `0 4 * * *` |
| 18:00 | 10:00 | `0 10 * * *` |

在线工具: https://crontab.guru/

---

## 📊 监控运行状态

### 添加Status Badge

在 `README.md` 顶部添加：

```markdown
![Daily News](https://github.com/你的用户名/training-news/actions/workflows/daily_news.yml/badge.svg)
```

这会显示工作流的运行状态。

### 查看运行历史

Actions页面可以看到所有运行记录，点击可查看详细日志。

---

## 🎨 自定义网站样式

编辑 `src/html_generator.py` 中的CSS样式，修改：

- 颜色主题（`--primary-color`, `--secondary-color`）
- 字体大小
- 布局样式
- 动画效果

---

## 💡 进阶功能

### 添加更多RSS源

编辑 `src/config.py`：

```python
RSS_SOURCES = [
    {
        'name': '网站名称',
        'url': 'https://example.com/feed',
        'category': '分类',
        'description': '描述'
    },
    # 添加更多...
]
```

**如何找RSS源**：
- 网站底部查找RSS图标
- 使用 RSSHub: https://docs.rsshub.app/
- 使用 Feed43 生成RSS: https://feed43.com/

### 推送到Telegram

替代邮件推送，可以推送到Telegram：

1. 创建Telegram Bot（找 @BotFather）
2. 获取Bot Token和Chat ID
3. 修改 `src/email_sender.py` 改用Telegram API

### 添加数据分析

可以统计：
- 每日文章数量趋势
- 热门分类
- 来源分布

在 `src/html_generator.py` 中添加图表展示。

---

## 📞 获取帮助

如果遇到问题：

1. 查看本文档的"常见问题排查"部分
2. 查看GitHub Actions运行日志
3. 在GitHub仓库提Issue
4. 加入讨论组寻求帮助

---

**祝你使用愉快！如果觉得有用，别忘了给项目点个Star⭐️**
