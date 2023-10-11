#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身
可以构造一个MIMEMultipart对象代表邮件本身
然后往里面加上一个MIMEText作为邮件正文
再继续往里面加上表示附件的MIMEBase对象即可"""


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart

import smtplib


def _format_addr(s):
    """格式化邮件地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))

from_addr = input('发件人地址：')  # yj1516268@163.com
password = input('邮箱密码：')
to_addr = input('收件人地址：')   # 1339670004@qq.com
smtp_server = input('SMTP服务器地址：')   # smtp.163.com

# 邮件对象
msg = MIMEMultipart()   # 基类
msg['From'] = _format_addr("略略略 <%s>" % from_addr)
msg['To'] = _format_addr("管理员 <%s>" % to_addr)
msg['Subject'] = Header("来自SMTP的信息...", "utf-8").encode()

# 添加邮件正文，邮件正文是MIMEText
msg.attach(MIMEText("Send whith file...", "plain", "utf-8"))

# 添加附件
'''就是加上一个MIMEBASE，从本地读取一个图片'''
with open("./images/2B.gif", 'rb') as file:
    # 设置附件的MIME和文件名，这里是gif格式
    mime = MIMEBase("image", "gif", filename="2B.gif")
    # 加上必要的头信息
    mime.add_header("Content-Disposition", "attachment", filename="2B.gif")
    mime.add_header("Content-ID", "<0>")
    mime.add_header('X-Attachment-Id', '0')
    # 读进附件内容
    mime.set_payload(file.read())
    # 用Base64编码
    encoders.encode_base64(mime)
    # 添加附件到MIMEMultipart
    msg.attach(mime)


# 发送
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认25端口
# 打印和SMTP服务器交互的所有信息,SMTP协议就是简单的文本命令和响应
server.set_debuglevel(1)
server.login(from_addr, password)   # 登录SMTP服务器
# 发送邮件，可以多发，所以用list，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()