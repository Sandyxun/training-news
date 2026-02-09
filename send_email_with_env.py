#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 .env 文件读取配置并发送邮件
"""

import os
import sys

def load_env_file(env_file='.env'):
    """从.env文件加载环境变量"""
    if not os.path.exists(env_file):
        return False

    print(f"[INFO] 从 {env_file} 加载配置...")
    with open(env_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 跳过注释和空行
            if not line or line.startswith('#'):
                continue

            # 解析环境变量
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value

    return True

def check_config():
    """检查配置是否完整"""
    sender = os.getenv('SENDER_EMAIL', '').strip()
    password = os.getenv('EMAIL_PASSWORD', '').strip()
    receiver = os.getenv('RECEIVER_EMAIL', '').strip()

    if not (sender and password and receiver):
        print("[ERROR] 邮件配置不完整")
        print("\n请确保以下环境变量已设置：")
        print("  SENDER_EMAIL - 发件人邮箱")
        print("  EMAIL_PASSWORD - 邮箱密码")
        print("  RECEIVER_EMAIL - 收件人邮箱")
        print("\n你可以：")
        print("  1. 创建 .env 文件并填写配置（参考 .env.template）")
        print("  2. 或设置系统环境变量")
        return False

    print("[OK] 配置检查通过")
    print(f"  发件人: {sender}")
    print(f"  收件人: {receiver}")
    return True

def send_email():
    """发送邮件"""
    sys.path.insert(0, 'src')
    from email_sender import EmailSender

    print("\n" + "=" * 60)
    print("开始发送邮件...")
    print("=" * 60 + "\n")

    sender = EmailSender()
    success = sender.send_email()

    if success:
        print("\n" + "=" * 60)
        print("[SUCCESS] 邮件推送成功！")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("[FAIL] 邮件推送失败")
        print("=" * 60)

    return success

def main():
    print("\n" + "=" * 60)
    print("企业人才发展与AI资讯 - 邮件推送")
    print("=" * 60 + "\n")

    # 尝试从 .env 文件加载配置
    if os.path.exists('.env'):
        load_env_file('.env')
    else:
        print("[INFO] 未找到 .env 文件，使用系统环境变量")

    # 检查配置
    if not check_config():
        return False

    # 发送邮件
    return send_email()

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n[ERROR] 发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
