@echo off
REM 邮件推送脚本
REM 请在下面设置你的邮件配置信息

echo ======================================================
echo 企业人才发展与AI资讯 - 邮件推送
echo ======================================================
echo.

REM 检查环境变量是否已设置
if "%SENDER_EMAIL%"=="" (
    echo [INFO] 环境变量未设置，请按照提示输入配置信息
    echo.

    set /p SENDER_EMAIL="请输入发件人邮箱（如 your_email@gmail.com）: "
    set /p EMAIL_PASSWORD="请输入邮箱密码或应用专用密码: "
    set /p RECEIVER_EMAIL="请输入收件人邮箱（多个用逗号分隔）: "
) else (
    echo [INFO] 使用已设置的环境变量
    echo 发件人: %SENDER_EMAIL%
    echo 收件人: %RECEIVER_EMAIL%
    echo.
)

REM 运行邮件发送
echo [INFO] 开始发送邮件...
python src\email_sender.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================
    echo [SUCCESS] 邮件发送成功！
    echo ======================================================
) else (
    echo.
    echo ======================================================
    echo [FAIL] 邮件发送失败，请检查配置和网络连接
    echo ======================================================
)

pause
