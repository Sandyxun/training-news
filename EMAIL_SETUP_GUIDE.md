# 邮件推送配置指南

## 方式一：使用 .env 文件（推荐）

### 步骤 1: 创建 .env 文件

复制模板文件：
```bash
copy .env.template .env
```

或手动创建 `.env` 文件，内容如下：
```
SENDER_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver@example.com
```

### 步骤 2: 填写配置信息

编辑 `.env` 文件，填入你的实际信息：

- **SENDER_EMAIL**: 发件人邮箱（建议Gmail）
- **EMAIL_PASSWORD**: 邮箱密码或应用专用密码
- **RECEIVER_EMAIL**: 收件人邮箱（多个用逗号分隔）

**Gmail 应用专用密码获取方式：**
1. 访问 Google 账户设置
2. 安全性 -> 两步验证
3. 应用专用密码 -> 生成新密码
4. 选择"邮件"和"Windows计算机"
5. 复制生成的16位密码

### 步骤 3: 运行邮件推送

```bash
python send_email_with_env.py
```

## 方式二：使用系统环境变量

### Windows PowerShell:
```powershell
$env:SENDER_EMAIL="your_email@gmail.com"
$env:EMAIL_PASSWORD="your_password"
$env:RECEIVER_EMAIL="receiver@example.com"
python src/email_sender.py
```

### Windows CMD:
```cmd
set SENDER_EMAIL=your_email@gmail.com
set EMAIL_PASSWORD=your_password
set RECEIVER_EMAIL=receiver@example.com
python src\email_sender.py
```

### 永久设置（Windows系统环境变量）:
1. 右键"此电脑" -> 属性 -> 高级系统设置
2. 环境变量 -> 用户变量 -> 新建
3. 分别添加三个变量：
   - SENDER_EMAIL
   - EMAIL_PASSWORD
   - RECEIVER_EMAIL

## 方式三：快速测试（不推荐）

如果你只是想快速测试，可以告诉我你的邮件配置，我可以帮你临时设置并发送。

## 当前状态

✅ RSS数据已采集（142篇文章）
✅ HTML页面已生成
✅ 推送报告已生成（push_report_20260209.html）
⏳ 等待邮件配置并发送

## 故障排查

### 问题1: 登录失败
- 确认邮箱地址和密码正确
- 如果使用Gmail，必须使用应用专用密码，不是账户密码
- 检查是否开启了两步验证

### 问题2: 连接超时
- 检查网络连接
- 确认防火墙没有拦截
- 某些地区可能无法访问Gmail SMTP服务器

### 问题3: 收不到邮件
- 检查垃圾邮件文件夹
- 确认收件人邮箱地址正确
- 查看发送日志确认是否发送成功

## 下一步

配置完成后，运行以下命令发送今日推送：

```bash
# 使用 .env 文件
python send_email_with_env.py

# 或直接运行（需要先设置环境变量）
python src/email_sender.py
```

邮件内容包括：
- 今日资讯总数：142篇
- AI相关：62篇
- 科技商业：58篇
- 技术：20篇
- 企业学习：2篇

精美的HTML格式，按分类组织，易于阅读。
