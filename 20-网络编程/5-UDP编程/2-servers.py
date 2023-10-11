#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""servers for UDP"""

import socket

# 服务器首先需要绑定端口：
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # SOCK_DGRAM指定使用UDP
s.bind(('0.0.0.0', 9986))  # 绑定端口
'''不需要调用listen()方法监听，直接接收来自任何客户端的数据'''

print('[info]:已建立UDP连接...')
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)  # 返回数据以及客户端地址和端口
    print('[info]:接收来自 <{}:{}> 的数据: {}'.format(addr[0], addr[1], data))  # 接收数据
    s.sendto(('数据原样返回: %s' % data.decode('utf-8')).encode('utf-8'),
             addr)  # 将数据用UDP发送到客户端
