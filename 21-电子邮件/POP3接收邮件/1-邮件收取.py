#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上
收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3
Py内置poplib模块，实现了POP3协议，可以直接用来收邮件
POP3协议收取的不是已经可以阅读的邮件，而是邮件的原始文本
这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本
要把POP3收取的文本变成可以阅读的邮件
还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象
所以，收取邮件分两步：
第一步：用poplib把邮件的原始文本下载到本地；
第二部：用email解析原始文本，还原为邮件对象"""


from email.parser import Parser
from email.utils import parseaddr
from email.header import decode_header

import poplib


"""通过POP3下载邮件"""

# 输入邮件地址，口令和POP3服务器地址
email = input("邮箱地址：")  # 1339670004@qq.com
pwd = input("邮箱密码：")    # hrhgglctlpoygddb
pop3_server = input("POP3服务器地址：")   # pop.qq.com，端口110


def guess_charset(msg):
    """文本邮件的内容也是str，还需要检测编码，否则非UTF-8编码的邮件都无法正常显示"""
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get("Content-Type", '').lower()
        pos = content_type.find("charset=")
        if pos >= 0:
            charset = content_type[pos + 8].strip()
    return charset


def decode_str(s):
    """邮件的Subject或Email中包含的名字都是经过编码后的str，要正常显示就必须decode"""
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
'''decode_header()返回一个list
因为像Cc、Bcc这样的字段可能包含多个邮件地址，所以解析出来的会有多个元素
decode_str()函数只取了第一个元素，懒！'''


# 但是这个Message对象本身可能是一个MIMEMultipart对象
'''即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层
所以要递归地打印出Message对象的层次结构'''
def print_info(msg, indent=0):   # indent用于缩进显示
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == "Subject":
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print("%s%s: %s" % (' ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print("%spart %s" % (' ' * indent, n))
            print("%s---------" % (' '* indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print("%sText: %s" % (' ' * indent, content + '...'))
        else:
            print("%sAttachment: %s" % (' ' * indent, content_type))

# 连接到POP3服务器，要使用SSL加密连接
server = poplib.POP3_SSL(pop3_server)
# 打开调试信息
server.set_debuglevel(1)
# 可选：打印POP3服务器的欢迎文字
print(server.getwelcome().decode("utf-8"))

# 身份认证
server.user(email)
server.pass_(pwd)

# stat()返回邮件数量和占用空间
print("邮件数量：%s. 所占空间：%s" % server.stat())
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 返回的列表类似:[b'1 82923', b'2 2184', ...]
print(mails)

# 获取最新一封邮件
'''注意索引号从1开始'''
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件原始文本的第一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode("utf-8")

"""解析邮件——解析邮件的过程和构造邮件正好相反"""

# 把邮件内容解析为Message对象
msg = Parser().parsestr(msg_content)
print_info(msg)

# 可以根据邮件索引号直接从服务器删除邮件：
'''server.dele(index)'''

# 关闭连接
server.close()