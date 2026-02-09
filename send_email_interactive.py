#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
交互式邮件推送脚本
如果环境变量未设置，将提示用户输入
"""

import os
import sys

def setup_environment():
    """设置环境变量"""

    # 检查是否已有环境变量
    sender = os.getenv('SENDER_EMAIL', '').strip()
    password = os.getenv('EMAIL_PASSWORD', '').strip()
    receiver = os.getenv('RECEIVER_EMAIL', '').strip()

    if sender and password and receiver:
        print("[INFO] 使用已设置的环境变量")
        print(f"发件人: {sender}")
        print(f"收件人: {receiver}")
        return True

    print("\n" + "=" * 60)
    print("邮件配置向导")
    print("=" * 60)
    print("\n[INFO] 环境变量未设置，请输入邮件配置信息\n")

    # 获取用户输入
    if not sender:
        sender = input("请输入发件人邮箱（如 your_email@gmail.com）: ").strip()
        os.environ['SENDER_EMAIL'] = sender

    if not password:
        print("\n提示：如果使用Gmail，需要使用应用专用密码，而不是账户密码")
        print("应用专用密码获取方式：Google账户 -> 安全性 -> 两步验证 -> 应用专用密码")
        password = input("\n请输入邮箱密码或应用专用密码: ").strip()
        os.environ['EMAIL_PASSWORD'] = password

    if not receiver:
        receiver = input("请输入收件人邮箱（多个用逗号分隔）: ").strip()
        os.environ['RECEIVER_EMAIL'] = receiver

    if not (sender and password and receiver):
        print("\n[ERROR] 配置信息不完整，无法发送邮件")
        return False

    print("\n[OK] 配置完成！")
    return True

def send_email():
    """发送邮件"""
    # 导入邮件发送模块
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
        print("[FAIL] 邮件推送失败，请检查：")
        print("1. 邮箱地址和密码是否正确")
        print("2. 如果使用Gmail，是否使用了应用专用密码")
        print("3. 网络连接是否正常")
        print("4. 邮件服务器是否可访问")
        print("=" * 60)

    return success

def main():
    print("\n" + "=" * 60)
    print("企业人才发展与AI资讯 - 邮件推送")
    print("=" * 60)

    # 设置环境变量
    if not setup_environment():
        return

    # 发送邮件
    send_email()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[INFO] 用户取消操作")
    except Exception as e:
        print(f"\n[ERROR] 发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
