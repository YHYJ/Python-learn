#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""在1-urlopen.py中，urlopen()的参数就是一个URL地址
如果需要执行更复杂的操作，比如增加HTTP报头，必须创建一个 Request 实例来作为urlopen()的参数
将需要访问的URL地址作为Request实例的参数"""


import urllib2


request = urllib2.Request("http://yj1516.site")  # 构造并返回一个 Request 对象

response = urllib2.urlopen(request)  # Request 对象作为urlopen()方法的参数，发送给服务器并接收响应


html = response.read()

print html
