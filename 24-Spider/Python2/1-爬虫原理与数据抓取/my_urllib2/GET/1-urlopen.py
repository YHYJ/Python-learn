#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib2是Python2.7自带的模块"""

import urllib2


response = urllib2.urlopen("http://yj1516.site")    # 向指定URl发送请求，并返回服务器响应的类文件对象

html = response.read()  # 类文件对象支持真正的文件对象的操作方式，如 read() 方法读物取文件全部内容，返回字符串

print html
