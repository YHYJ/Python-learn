#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""SMTP是发送邮件的协议，Py内置对SMTP的支持
可以发送纯文本邮件、HTML邮件以及带附件的邮件
Py对SMTP支持有smtplib和email两个模块
email构造邮件，smtplib发送邮件"""


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


import smtplib


def _format_addr(s):
    """格式化邮件地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))   # Header对中文进行编码


# 输入通过SMTP发送的地址：
from_addr = input('发件人地址：')
password = input('邮箱密码：')
to_addr = input('收件人地址：')
smtp_server = input('SMTP服务器地址：')
matter = input('邮件内容：')


# 构造一个最简单的纯文本邮件：
msg = MIMEText("%s" % matter, 'plain', 'utf-8')
'''第一个参数为邮件正文
第二个参数是MIME的图表类型(subtype)，'plain'表示纯文本，最终的MIME就是'text/plain'
第三个参数指定utf-8编码'''
msg['From'] = _format_addr("略略略 <%s>" % from_addr)  # 发件人信息
msg['To'] = _format_addr("管理员 <%s>" % to_addr)  # 接收str而非list，多个地址逗号分割
msg['Subject'] = Header("来自您弟弟的信息...", "utf-8").encode()


# 发送
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认25端口
# 打印和SMTP服务器交互的所有信息,SMTP协议就是简单的文本命令和响应
server.set_debuglevel(1)
server.login(from_addr, password)   # 登录SMTP服务器
# 发送邮件，可以多发，所以用list，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
