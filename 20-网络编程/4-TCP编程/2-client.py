#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""大多数连接都是可靠的TCP连接
创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器

当在浏览器中访问新浪时，PC机就是客户端
浏览器会主动向新浪的服务器发起连接
如果一切顺利，新浪的服务器接受了这个连接，一个TCP连接就建立起来了
后面的通信就是发送网页内容了"""


import socket

# 创建一个基于TCP连接的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 创建一个socket
s.connect(("www.sina.com.cn", 80))  # 建立连接，参数是一个tuple，包含地址和端口号
'''创建Socket时，AF_INET指定使用IPv4协议
如果要用更先进的IPv6，就指定为AF_INET6
SOCK_STREAM指定使用面向流的TCP协议
这样一个Socket对象就创建成功，但是还没有建立连接'''
'''客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号：
新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址
而作为服务器，提供什么样的服务，端口号就必须固定下来
由于想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口
因为80端口是Web服务的标准端口
其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口等等
端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
'''

# 请求数据
'''建立TCP连接后就可以向新浪服务器发送请求，要求返回首页的内容'''
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\n'
       b'Connection: close\r\n\r\n')    # 发送数据
'''TCP连接创建的是双向通道，双方都可以同时给对方发数据
但是谁先发谁后发，怎么协调，要根据具体的协议来决定
例如HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端
发送的文本格式必须符合HTTP标准，格式没问题就可以接收新浪服务器返回的数据了'''

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
'''接收数据调用recv(max)方法，一次最多接收max指定的字节数
在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环
'''
s.close()   # 关闭Socket连接

# 处理数据
'''接收到的数据包括HTTP头和网页本身，打印HTTP头，保存网页内容到文件'''
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
'''接收的数据写入html文件'''
with open('./Data/sina.html', 'wb') as f:
    f.write(html)
