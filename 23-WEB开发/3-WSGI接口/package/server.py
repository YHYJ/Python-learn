#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-11 20:05:32
Last modified: 2017-09-11 20:05:32
Python release: 3.6.2

负责启动WSGI服务器以加载application()函数
"""

from wsgiref.simple_server import make_server

from hello_1 import application

# 创建一个服务器，IP地址为空，端口为8000，处理函数是application
IP = ''
Port = 8000
httpd = make_server(IP, Port, application)
print('Serving HTTP on port %d...' % Port)
# 开始监听HTTP请求
httpd.serve_forever()

