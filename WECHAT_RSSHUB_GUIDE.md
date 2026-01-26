# 微信公众号订阅指南 - 使用RSSHub

本指南将帮助你订阅微信公众号（如"培训经理指南"、"培训江湖"等）到你的资讯推送系统。

---

## 📖 什么是RSSHub？

[RSSHub](https://docs.rsshub.app/) 是一个开源项目，可以为各种网站（包括微信公众号）生成RSS订阅源。

**特点**：
- 完全免费
- 支持微信公众号、知乎、微博等
- 有公共实例，也可以自己部署

---

## 🚀 方法一：使用公共RSSHub实例（最简单）

### 步骤1：获取公众号的Biz参数

微信公众号的RSS地址格式：
```
https://rsshub.app/wechat/mp/homepage/{biz}
```

其中 `{biz}` 是公众号的唯一标识。

#### 如何获取Biz参数？

**方法A：通过搜狗微信搜索**

1. 访问 [搜狗微信搜索](https://weixin.sogou.com/)
2. 搜索公众号名称（如"培训经理指南"）
3. 点击进入公众号主页
4. 查看浏览器地址栏URL，找到 `__biz=` 后面的参数

   示例：
   ```
   https://mp.weixin.qq.com/profile?src=3&timestamp=xxx&ver=1&signature=xxx&__biz=MzAwNDQ0MDk3Mg==
   ```

   `biz` 参数就是：`MzAwNDQ0MDk3Mg==`

5. 完整的RSS地址就是：
   ```
   https://rsshub.app/wechat/mp/homepage/MzAwNDQ0MDk3Mg==
   ```

**方法B：使用Chrome扩展**

1. 安装 [RSSHub Radar](https://github.com/DIYgod/RSSHub-Radar) 扩展
2. 打开微信公众号文章页面
3. 扩展会自动识别并显示RSS地址

**方法C：手动从文章链接提取**

1. 打开任意一篇该公众号的文章
2. 查看文章URL中的 `__biz` 参数

### 步骤2：验证RSS地址是否可用

在浏览器中访问生成的RSS地址，检查是否能看到文章列表：
```
https://rsshub.app/wechat/mp/homepage/你的biz参数
```

如果看到XML格式的RSS内容，说明配置成功！

### 步骤3：添加到配置文件

编辑 `src/config.py`，在 `RSS_SOURCES` 列表中添加：

```python
RSS_SOURCES = [
    # ... 其他源 ...

    # 培训经理指南
    {
        'name': '培训经理指南',
        'url': 'https://rsshub.app/wechat/mp/homepage/你获取的biz参数',
        'category': '培训管理',
        'description': '培训经理的实战指南'
    },

    # 培训江湖
    {
        'name': '培训江湖',
        'url': 'https://rsshub.app/wechat/mp/homepage/你获取的biz参数',
        'category': '培训行业',
        'description': '培训行业资讯与观点'
    },
]
```

---

## 🔧 方法二：自建RSSHub（推荐，更稳定）

如果公共实例不稳定，可以自己部署RSSHub。

### 使用Docker部署（最简单）

```bash
# 1. 安装Docker（如果还没有）
# 访问 https://www.docker.com/ 下载安装

# 2. 运行RSSHub容器
docker run -d --name rsshub -p 1200:1200 diygod/rsshub

# 3. 访问 http://localhost:1200 验证
```

### 使用Vercel免费部署

1. Fork [RSSHub仓库](https://github.com/DIYgod/RSSHub)
2. 在 [Vercel](https://vercel.com/) 注册账号
3. 导入你Fork的仓库
4. 部署完成后，Vercel会给你一个域名，如 `your-rsshub.vercel.app`

### 修改配置使用自己的实例

编辑 `src/config.py`：

```python
# 使用自己的RSSHub实例
RSSHUB_BASE_URL = 'https://your-rsshub.vercel.app'  # 或 http://localhost:1200

RSS_SOURCES = [
    {
        'name': '培训经理指南',
        'url': f'{RSSHUB_BASE_URL}/wechat/mp/homepage/biz参数',
        'category': '培训管理',
        'description': '培训经理的实战指南'
    },
]
```

---

## 📋 常见培训类公众号Biz获取清单

以下是一些建议订阅的公众号（需要你自己获取biz参数）：

| 公众号名称 | 类别 | 说明 |
|-----------|------|------|
| 培训经理指南 | 培训管理 | 培训经理的实战指南和工具 |
| 培训江湖 | 培训行业 | 培训行业资讯与观点分享 |
| 培训杂志 | 培训产业 | 培训行业专业期刊 |
| ATD中国 | 人才发展 | ATD在中国的官方账号 |
| CLO首席学习官 | 企业学习 | 企业学习与发展 |
| 培训人社区 | 培训社群 | 培训从业者社区 |
| HR实名俱乐部 | 人力资源 | HR与人才发展 |
| 组织发展OD | 组织发展 | 组织发展专业内容 |

---

## ⚠️ 重要提示

### RSSHub公共实例的限制

- 公共实例可能不稳定，偶尔无法访问
- 部分公众号可能更新不及时
- 建议自建实例以获得更好体验

### 微信限制

- 部分公众号可能无法通过RSSHub订阅
- 订阅的是公众号的公开文章，不包括会员内容
- 如果公众号改版，可能影响抓取

### 解决方案

如果RSSHub无法使用，可以考虑：

1. **改用其他RSS生成服务**
   - Feed43: https://feed43.com/
   - FetchRSS: https://fetchrss.com/

2. **手动爬虫**
   - 修改 `rss_collector.py` 添加自定义爬虫
   - 爬取搜狗微信搜索结果

3. **使用API服务**（可能需要付费）
   - 微信公众号API
   - 第三方数据服务

---

## 🧪 测试配置

配置完成后，测试是否工作：

```bash
# 进入项目目录
cd D:\projects\training-news\src

# 运行采集脚本
python rss_collector.py
```

查看输出，确认公众号文章是否成功采集。

---

## 📞 获取帮助

如果遇到问题：

1. **查看RSSHub文档**：https://docs.rsshub.app/social-media.html#wei-xin
2. **RSSHub Telegram群**：https://t.me/rsshub
3. **GitHub Issues**：https://github.com/DIYgod/RSSHub/issues

---

## 💡 快速配置示例

假设你已经获取到了"培训经理指南"的biz为 `MzAwNDQ0MDk3Mg==`：

```python
# src/config.py

RSS_SOURCES = [
    # 现有的国际源...

    # 添加微信公众号
    {
        'name': '培训经理指南',
        'url': 'https://rsshub.app/wechat/mp/homepage/MzAwNDQ0MDk3Mg==',
        'category': '培训管理',
        'description': '培训经理的实战指南'
    },
]
```

保存后提交到GitHub，系统会自动采集这个公众号的文章。

---

**祝你配置顺利！如有问题随时询问。**
