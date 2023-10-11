#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Handler处理器和自定义opener()
urlopen()方法是 urllib2.OpenerDirector 的实例，它是一个特殊的opener（模块构建好的）
但是urlopen()方法不支持代理、Cookie等其他 HTTP/HTTPS 高级功能。如果要支持这些功能：
    1. 使用相关的 Handler 处理器创建特定功能的处理器对象
    2. 通过 urllib2.build_opener() 方法使用这些处理器对象，创建自定义 opener 对象
    3. 使用自定义的 opener 对象，调用 open() 方法发送请求
注意：如果程序里所有的请求都使用自定义的opener
     可以使用 urllib2.install_opener() 将自定义的 opener 对象定义为全局opener
     表示如果之后凡是调用urlopen，都将使用这个opener（根据需求选择）。
"""

import random
import urllib2

from conf.User_Agent_list import USER_AGENT_LIST


# 自定义简单的opener()
'''构建一个 HTTPHandler 处理器对象，支持处理HTTP请求'''
http_handler = urllib2.HTTPHandler(debuglevel=1)   # 打开Debug Log，输出报头


# 调用 build_opener() 方法创建支持HTTP请求的opener对象
opener = urllib2.build_opener(http_handler)


# 构建 Request 请求
url = "http://www.baidu.com/"
headers = {"User-Agent": random.choice(USER_AGENT_LIST)}

request = urllib2.Request(url, headers=headers)


# 调用自定义 opener 对象的 open() 方法，发送request请求
response = opener.open(request)


print response.read()
