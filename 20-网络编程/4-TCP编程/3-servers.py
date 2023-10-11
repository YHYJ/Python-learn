#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""服务器进程首先绑定一个端口并监听来自其他客户端的连接
如果某个客户端连接过来了，服务器就与该客户端建立Socket连接
随后的通信就靠这个Socket连接
服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接
由于服务器会有大量来自客户端的连接
所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的
一个Socket依赖4项 ——
服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket
但是服务器还需要同时响应多个客户端的请求
所以，每个连接都需要一个新的进程或者新的线程来处理
否则，服务器一次就只能服务一个客户端了"""


import socket
import threading
import time

# 编写一个简单的服务器程序
'''它接收客户端连接，把客户端发来的字符串加上'Hello'再发出去'''

# 创建一个基于IPV4和TCP协议的Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听的地址和端口
'''服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上
也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址
如果绑定到本机地址，客户端必须同时在本机运行才能连接
也即外部的计算机无法连接进来
端口号需要预先指定，因为这个服务不是标准服务，所以用9999这个端口号
小于1024的端口号必须要有管理员权限才能绑定'''
server_socket.bind(('127.0.0.1', 9999))  # 绑定本机地址和9999端口
server_socket.listen(5)  # 开始监听，参数指定等待连接的最大数量，转换为被动socket，只能链接client_socket，不能收发信息
print('[info]:waiting for connection...')

# 每个连接都必须创建新线程/进程处理
'''单线程在处理连接的过程中无法接受其他客户端的连接'''


def tcplink(cs_socket, server_addr):
    print("Accept new connection from %s:%s..." % server_addr)
    cs_socket.send('Welcome!'.encode('utf-8'))  # send()通过Socket发送字符串到客户端
    while True:
        data = cs_socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            cs_socket.close()
            break
        print('[info]:Connection from %s:%s closed.' % server_addr)
        cs_socket.send('Hello, %s!' % data.decode('utf-8').encode('utf-8'))

# 通过一个永久循环接受来自客户端的连接
while True:
    # 接受一个新连接:
    cs_socket, server_addr = server_socket.accept()  # accept()等待并返回一个客户端的连接
    # 创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink, args=(cs_socket, server_addr))
    t.start()
