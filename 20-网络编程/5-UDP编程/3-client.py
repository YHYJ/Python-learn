#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""client for UDP"""


import socket

# 首先创建基于UDP的Socket
'''不需要调用connect()，直接通过sendto()给服务器发数据'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)
#  s.connect(('127.0.0.1', 9986))
datas = []

while True:
    into = input('请输入(q完成)数据：')
    if into != 'q':
        datas.append(into.encode('utf-8'))
    else:
        break
for data in datas:
    s.sendto(data, ('127.0.0.1', 9986))  # 不需要connect，直接发送到指定地址
    #  s.send(data)                      # send和connect配合使用，当没有服务器bind到指定端口时立即报错
    print(s.recv(1024).decode('utf-8'))  # 接收数据
s.close()
