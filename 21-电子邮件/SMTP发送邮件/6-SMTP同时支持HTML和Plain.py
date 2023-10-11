#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""发送HTML的同时再附加一个纯文本
如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
利用MIMEMultipart就可以组合一个HTML和Plain
要注意指定subtype是alternative"""


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
from_addr = input('发件人地址：')  # yj1516268@163.com
password = input('邮箱密码：')
to_addr = input('收件人地址：')   # 1339670004@qq.com
smtp_server = input('SMTP服务器地址：')   # smtp.163.com
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
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认25端口
# 打印和SMTP服务器交互的所有信息,SMTP协议就是简单的文本命令和响应
server.set_debuglevel(1)
server.login(from_addr, password)   # 登录SMTP服务器
# 发送邮件，可以多发，所以用list，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
