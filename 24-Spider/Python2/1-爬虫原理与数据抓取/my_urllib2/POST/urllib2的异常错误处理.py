#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用urlopen或opener.open方法发出一个请求时
如果urlopen或opener.open不能处理这个response，就产生错误

这里主要说的是URLError和HTTPError，以及对它们的错误处理
"""

import urllib2


# URLError
"""产生原因"""
'''
1. 无网络连接
2. 服务器连接失败
3. 找不到指定服务器
'''
'''访问一个不存在的域名'''
request = urllib2.Request("http://qaqnnovo.com")

try:
    response = urllib2.urlopen(request, timeout=5)
except urllib2.URLError as e:
    print(e)

print("----------- 1 -----------")

# HTTPError
"""产生原因"""
'''urlopen 或 opener.open不能处理response包含的响应状态吗'''
"""urllib2 可以处理3开头的重定向响应，100-299表示成功，所以只要处理400-599的响应码"""
request = urllib2.Request("http://itcast.cn/c9")

try:
    response = urllib2.urlopen(request, timeout=5)
except urllib2.HTTPError as e:
    print(e)

print("----------- 2 -----------")

# 改进
"""由于URLError是HTTPError的父类，所以父类的异常应当写到子类的异常后面"""
request = urllib2.Request("http://itcast.cn/c9")

try:
    response = urllib2.urlopen(request, timeout=5)
except urllib2.HTTPError as e:
    print(e.code)
    print(e)
except urllib2.URLError as e:
    print(e)
else:
    print("<OK:> No Question")
