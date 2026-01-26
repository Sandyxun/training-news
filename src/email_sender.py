"""
邮件发送模块 - 发送每日资讯邮件
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json
from config import EMAIL_CONFIG, NEWS_FILE


class EmailSender:
    def __init__(self):
        # 从环境变量读取敏感信息
        self.smtp_server = EMAIL_CONFIG['smtp_server']
        self.smtp_port = EMAIL_CONFIG['smtp_port']
        self.sender_email = os.getenv('SENDER_EMAIL', '')
        self.sender_password = os.getenv('EMAIL_PASSWORD', '')  # Gmail应用专用密码
        # 支持多个收件人，用逗号分隔
        receiver_emails = os.getenv('RECEIVER_EMAIL', '')
        self.receiver_emails = [email.strip() for email in receiver_emails.split(',') if email.strip()]

    def load_news_data(self):
        """
        加载新闻数据
        """
        try:
            with open(NEWS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"加载新闻数据失败: {str(e)}")
            return None

    def generate_html_email(self, news_data):
        """
        生成HTML格式的邮件内容
        """
        articles = news_data.get('articles', [])
        total = news_data.get('total', 0)
        update_time = news_data.get('update_time', '')

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f5f5f5;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                    margin-bottom: 20px;
                }}
                .header h1 {{
                    margin: 0;
                    font-size: 28px;
                }}
                .header p {{
                    margin: 10px 0 0 0;
                    opacity: 0.9;
                }}
                .stats {{
                    background: white;
                    padding: 15px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                    text-align: center;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .article {{
                    background: white;
                    padding: 20px;
                    margin-bottom: 15px;
                    border-radius: 8px;
                    border-left: 4px solid #667eea;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    transition: transform 0.2s;
                }}
                .article:hover {{
                    transform: translateX(5px);
                }}
                .article h3 {{
                    margin: 0 0 10px 0;
                    color: #2c3e50;
                }}
                .article h3 a {{
                    color: #2c3e50;
                    text-decoration: none;
                }}
                .article h3 a:hover {{
                    color: #667eea;
                }}
                .meta {{
                    color: #7f8c8d;
                    font-size: 14px;
                    margin-bottom: 10px;
                }}
                .category {{
                    display: inline-block;
                    background: #667eea;
                    color: white;
                    padding: 2px 10px;
                    border-radius: 12px;
                    font-size: 12px;
                    margin-right: 10px;
                }}
                .summary {{
                    color: #555;
                    line-height: 1.6;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    padding: 20px;
                    color: #7f8c8d;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>📚 培训行业每日资讯</h1>
                <p>今天也要关注教育行业动态哦 ~</p>
            </div>

            <div class="stats">
                <strong>📊 今日资讯: {total} 篇</strong> |
                更新时间: {datetime.fromisoformat(update_time).strftime('%Y-%m-%d %H:%M')}
            </div>
        """

        # 添加文章
        if articles:
            for i, article in enumerate(articles, 1):
                published_time = datetime.fromisoformat(article['published']).strftime('%m-%d %H:%M')
                html += f"""
                <div class="article">
                    <h3>{i}. <a href="{article['link']}" target="_blank">{article['title']}</a></h3>
                    <div class="meta">
                        <span class="category">{article['category']}</span>
                        <span>{article['source']}</span> ·
                        <span>{published_time}</span>
                    </div>
                    <div class="summary">{article['summary']}</div>
                </div>
                """
        else:
            html += """
            <div class="article">
                <p>今天暂无新资讯</p>
            </div>
            """

        html += """
            <div class="footer">
                <p>🤖 本邮件由 GitHub Actions 自动生成并发送</p>
                <p>如需查看历史资讯，请访问项目网站</p>
            </div>
        </body>
        </html>
        """

        return html

    def send_email(self):
        """
        发送邮件
        """
        # 验证配置
        if not all([self.sender_email, self.sender_password, self.receiver_emails]):
            print("错误: 邮件配置不完整，请设置环境变量")
            print("需要设置: SENDER_EMAIL, EMAIL_PASSWORD, RECEIVER_EMAIL")
            return False

        # 加载新闻数据
        news_data = self.load_news_data()
        if not news_data:
            print("错误: 无法加载新闻数据")
            return False

        try:
            # 创建邮件
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"📚 企业人才发展每日资讯 - {datetime.now().strftime('%Y年%m月%d日')}"
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(self.receiver_emails)  # 支持多个收件人

            # 生成HTML内容
            html_content = self.generate_html_email(news_data)
            html_part = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(html_part)

            # 发送邮件
            print("正在连接邮件服务器...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            print(f"✓ 邮件发送成功！发送到: {', '.join(self.receiver_emails)}")
            return True

        except Exception as e:
            print(f"✗ 邮件发送失败: {str(e)}")
            return False


if __name__ == '__main__':
    sender = EmailSender()
    sender.send_email()
