#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用标准的25端口连接SMTP服务器时，使用的是明文传输
发送邮件的整个过程可能会被窃听
要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接
然后再使用SMTP协议发送邮件
某些邮件服务商，如Gmail提供的SMTP服务必须要加密传输"""


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

import smtplib


def _format_addr(s):
    """格式化邮件地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))   # Header对中文进行编码


# 输入通过SMTP发送的地址：
from_addr = "yj1516268@gmail.com"
password = input('邮箱密码：')
to_addr = input('收件人地址：')   # 1339670004@qq.com
smtp_server = "smtp.gmail.com"
# matter = input('邮件内容：')


# 邮件对象
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr("略略略 <%s>" % from_addr)  # 发件人信息
msg['To'] = _format_addr("管理员 <%s>" % to_addr)  # 接收str而非list，多个地址逗号分割
msg['Subject'] = Header("来自您弟弟的信息...", "utf-8").encode()


# 构造一个最简单的纯文本邮件：
msg.attach(MIMEText("欧拉", "plain", "utf-8"))
msg.attach(MIMEText("<html><body><h1>欧拉</h1></body></html>", 'html', 'utf-8'))


# 发送
server = smtplib.SMTP(smtp_server, 587)  # Gmail的SMTP端口是587
server.starttls()   # 创建SMTP后调用starttls()建立安全连接
# 打印和SMTP服务器交互的所有信息,SMTP协议就是简单的文本命令和响应
server.set_debuglevel(1)
server.login(from_addr, password)   # 登录SMTP服务器
# 发送邮件，可以多发，所以用list，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
