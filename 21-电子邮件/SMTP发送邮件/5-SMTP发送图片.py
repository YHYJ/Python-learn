#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""把一个图片嵌入到邮件正文中
只需按照发送附件的方式，先把邮件作为附件添加进去
然后在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了
如果有多个图片，给它们依次编号，然后引用不同的cid:x即可"""


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

# 把加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片
msg.attach(MIMEText("<html><body><h1>欧拉</h1>" +
                    "<p><img src='cid:0'></p>" +
                    "</body></html>", "html", "utf-8"))

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