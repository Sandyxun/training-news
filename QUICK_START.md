# 🚀 新手部署指南 - 5步完成

> 跟着这个文档，20分钟完成部署！

---

## 📌 准备工作

你需要：
- ✅ 一个Gmail邮箱
- ✅ 项目代码已在 `D:\projects\training-news`
- ⏱️ 约20-30分钟

---

## 第一步：注册GitHub账号（5分钟）

### 1. 打开GitHub官网

在浏览器中访问：**https://github.com**

### 2. 点击右上角"Sign up"（注册）

### 3. 填写注册信息

- **Email address**: 填写你的Gmail邮箱
- **Password**: 设置一个密码（至少15个字符，或8个字符包含数字和字母）
- **Username**: 用户名（英文，会显示在网址中）

### 4. 验证账号

- 完成人机验证（拼图）
- GitHub会发验证码到你的邮箱
- 输入验证码完成注册

### 5. 选择免费计划

- 问卷可以跳过（Skip）
- 选择"Free"免费计划

✅ **完成！你现在有GitHub账号了**

---

## 第二步：创建仓库（2分钟）

### 1. 点击右上角的"+"号，选择"New repository"

### 2. 填写仓库信息

```
Repository name:  training-news
Description:      企业人才发展每日资讯推送系统
```

### 3. 选择仓库类型

- ✅ 勾选 **Public**（公开仓库，才能免费使用GitHub Pages）

### 4. 不要勾选任何初始化选项

- ❌ 不勾选 "Add a README file"
- ❌ 不勾选 "Add .gitignore"
- ❌ 不勾选 "Choose a license"

### 5. 点击"Create repository"（创建仓库）

✅ **完成！仓库已创建**

你会看到一个页面显示如何上传代码。**先别关闭这个页面！**

---

## 第三步：上传代码（3分钟）

### 1. 复制仓库地址

在刚才的页面，找到类似这样的地址：
```
https://github.com/你的用户名/training-news.git
```

点击旁边的复制按钮📋

### 2. 打开命令提示符

按 `Win + R`，输入 `cmd`，回车

### 3. 运行以下命令

**⚠️ 把下面的"你的用户名"替换成你刚才注册的GitHub用户名**

```bash
cd D:\projects\training-news

git remote add origin https://github.com/你的用户名/training-news.git

git branch -M main

git push -u origin main
```

### 4. 输入GitHub账号密码

- Username: 你的GitHub用户名
- Password: **不是你的密码！需要用Token**

#### 如何获取Token？

1. 在GitHub网站，点击右上角头像 → **Settings**
2. 左侧最下面找到 **Developer settings**
3. 点击 **Personal access tokens** → **Tokens (classic)**
4. 点击 **Generate new token** → **Generate new token (classic)**
5. Note填写: `training-news`
6. Expiration选择: **No expiration**（不过期）
7. 勾选权限: ✅ **repo**（全部勾上）和 ✅ **workflow**
8. 滚动到底部，点击 **Generate token**
9. **⚠️ 复制生成的token并保存！**（只显示一次）

回到命令提示符，粘贴token作为密码

✅ **完成！代码已上传到GitHub**

刷新GitHub仓库页面，应该能看到所有文件了。

---

## 第四步：配置Gmail（5分钟）

### 1. 开启Gmail两步验证

1. 访问：**https://myaccount.google.com/security**
2. 找到"两步验证"
3. 点击开始，按照提示完成（需要手机号）

### 2. 生成应用专用密码

1. 访问：**https://myaccount.google.com/apppasswords**
2. 选择应用：**邮件**
3. 选择设备：**其他（自定义名称）**
4. 输入名称：`GitHub Actions`
5. 点击"生成"
6. **⚠️ 复制生成的16位密码**（格式如：abcd efgh ijkl mnop）

**把空格去掉，变成：abcdefghijklmnop**

✅ **完成！记住这个16位密码**

---

## 第五步：配置GitHub Secrets（3分钟）

### 1. 进入仓库的Settings

在你的GitHub仓库页面，点击上方的 **Settings** 标签

### 2. 找到Secrets设置

- 左侧菜单找到 **Secrets and variables**
- 点击展开，选择 **Actions**

### 3. 添加3个Secrets

点击 **New repository secret** 按钮，依次添加：

#### Secret 1: SENDER_EMAIL
- Name: `SENDER_EMAIL`
- Secret: `你的Gmail邮箱地址`（如 yourname@gmail.com）
- 点击 **Add secret**

#### Secret 2: EMAIL_PASSWORD
- Name: `EMAIL_PASSWORD`
- Secret: `刚才生成的16位应用专用密码`（去掉空格）
- 点击 **Add secret**

#### Secret 3: RECEIVER_EMAIL
- Name: `RECEIVER_EMAIL`
- Secret: `接收邮件的邮箱`（可以和发送邮箱一样）
- 点击 **Add secret**

✅ **完成！应该看到3个绿色的Secrets**

---

## 第六步：启用功能（2分钟）

### 1. 启用GitHub Actions

1. 点击仓库顶部的 **Actions** 标签
2. 如果看到提示，点击绿色按钮 **I understand my workflows, go ahead and enable them**

### 2. 配置GitHub Pages

1. 点击 **Settings** 标签
2. 左侧菜单找到 **Pages**
3. **Source** 选择：`Deploy from a branch`
4. **Branch** 选择：`gh-pages`（⚠️ 等会儿运行后才会出现）
5. Folder选择：`/ (root)`
6. 点击 **Save**

---

## 第七步：首次运行测试（3分钟）

### 1. 手动触发工作流

1. 点击 **Actions** 标签
2. 左侧选择"企业人才发展资讯每日推送"
3. 右侧点击 **Run workflow** 按钮
4. 再次点击绿色的 **Run workflow** 确认

### 2. 等待运行完成

- 会出现一个黄色圆圈，表示正在运行
- 等待2-3分钟，变成绿色✅表示成功
- 如果是红色❌表示失败，点进去查看日志

### 3. 检查结果

#### 查收邮件
- 打开你的Gmail邮箱
- 查看收件箱（也检查垃圾邮件文件夹）
- 应该收到一封"📚 企业人才发展每日资讯"的邮件

#### 查看网站
1. 回到Settings → Pages
2. 找到"Your site is live at ..."
3. 点击链接，打开你的资讯网站
4. 网址格式：`https://你的用户名.github.io/training-news`

---

## 🎉 完成！

如果邮件和网站都正常，说明部署成功！

### 后续使用

- ⏰ **自动运行**：每天早上9点自动推送
- 📧 **邮件通知**：直接发到你的邮箱
- 🌐 **网页查看**：随时访问网站查看历史资讯

### 如果失败了？

#### 邮件发送失败
1. 检查Secrets配置是否正确
2. 确认使用的是应用专用密码，不是Gmail密码
3. 查看Actions运行日志查找错误

#### 网站404
1. 等待5-10分钟（GitHub Pages需要部署时间）
2. 确认gh-pages分支已创建（在Code标签可以看到）
3. 重新保存Pages设置

#### 无法采集RSS
1. 可能是网络问题，稍后再试
2. 查看Actions日志看具体哪个源失败

---

## 🆘 需要帮助？

如果遇到问题：
1. 检查上面的步骤是否都完成
2. 查看Actions运行日志
3. 查看 `DEPLOYMENT.md` 获取更多详细说明

---

## 📌 快速回顾

```
1. 注册GitHub → 2. 创建仓库 → 3. 上传代码
→ 4. 配置Gmail → 5. 设置Secrets → 6. 启用功能
→ 7. 测试运行 → ✅ 完成！
```

**恭喜你！现在每天早上9点会自动收到资讯邮件了！**
