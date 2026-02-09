# 微信公众号配置指南

## 问题说明

你当前遇到的两个问题已解决：

### 1. 抓取数量限制问题 ✅ 已修复

**原因**:
- 代码原本限制每个源只抓取 10 条
- 并且只保留最近 7 天的文章

**修复方案**:
- 修改了 `src/rss_collector.py`，增加了可配置参数：
  - `max_articles`: 每个源最多抓取的文章数量（默认 30）
  - `days_back`: 抓取最近多少天的文章（默认 30 天）

**使用方法**:
```python
# 在主程序中，你可以这样调整参数：
collector = RSSCollector(max_articles=50, days_back=60)  # 抓取50条，60天内
articles = collector.collect_all()
```

### 2. 中文公众号无法抓取 🔧 需要配置

**原因**:
- 配置文件中只列出了公众号名称，没有实际的 RSS URL
- 微信公众号需要通过 RSSHub 服务获取 RSS，需要每个公众号的 `biz` 参数

**解决步骤**:

#### 步骤 1: 获取公众号的 biz 参数

你有两种方法获取 `biz` 参数：

**方法 1: 从公众号文章链接获取**

1. 在微信中打开任意一篇该公众号的文章
2. 点击右上角 `...` → `复制链接`
3. 链接格式类似：
   ```
   https://mp.weixin.qq.com/s?__biz=MzA3MDM3NjE5Mg==&mid=...
   ```
4. 其中 `__biz=` 后面的值就是 biz 参数（例如：`MzA3MDM3NjE5Mg==`）

**方法 2: 使用工具自动提取**

```bash
cd /d/projects/training-news
python src/wechat_helper.py
# 选择 2，然后粘贴文章链接
```

#### 步骤 2: 测试 biz 参数是否可用

```bash
python src/wechat_helper.py
# 选择 1，输入 biz 参数进行测试
```

如果测试成功，你会看到该公众号的最新文章列表。

#### 步骤 3: 添加到配置文件

编辑 `src/config.py`，找到微信公众号配置部分（约第 44-73 行），取消注释并替换 biz 参数：

```python
# 将这样的配置：
# {
#     'name': '培训经理指南',
#     'url': f'{RSSHUB_BASE_URL}/wechat/mp/homepage/YOUR_BIZ_HERE',
#     'category': '培训行业',
#     'description': '培训经理专业指南'
# },

# 改为（替换成你获取的 biz 参数）：
{
    'name': '培训经理指南',
    'url': f'{RSSHUB_BASE_URL}/wechat/mp/homepage/MzA3MDM3NjE5Mg==',
    'category': '培训行业',
    'description': '培训经理专业指南'
},
```

#### 步骤 4: 测试运行

```bash
cd /d/projects/training-news
python src/rss_collector.py
```

你应该能看到更多文章被抓取，包括中文公众号的内容。

## 常见问题

### Q: RSSHub 服务不可用怎么办？

A: 你可以自建 RSSHub 服务，或使用其他镜像：

```python
# 在 config.py 中修改：
RSSHUB_BASE_URL = 'https://your-rsshub-instance.com'
# 或者使用其他公共镜像（需要自行寻找）
```

### Q: 获取不到某个公众号的 biz 参数？

A: 确保：
1. 该公众号有发布过文章
2. 你复制的链接是完整的（包含 `__biz=` 参数）
3. 如果是企业号或订阅号，可能有不同的获取方式

### Q: 抓取到的文章还是很少？

A: 检查以下几点：
1. RSS 源是否正常（可以直接在浏览器中访问 RSS URL）
2. RSSHub 服务是否正常
3. 公众号是否有在最近 30 天内发布文章
4. 可以增加 `days_back` 参数获取更早的文章

## 推荐配置

对于培训行业资讯，推荐以下配置：

```python
# 采集更多历史文章
collector = RSSCollector(
    max_articles=50,    # 每个源抓取 50 条
    days_back=60        # 获取最近 60 天的文章
)
```

## 技术支持

如果遇到问题，请检查：
1. Python 环境和依赖是否安装正确：`pip install -r requirements.txt`
2. 网络连接是否正常
3. RSSHub 服务是否可访问

更多文档：
- RSSHub 官方文档：https://docs.rsshub.app/
- 项目 README：`README.md`
