#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib2
import cookielib


# 保存 cookie 的文件名
file_name = "cookie"


# 声明一个 MozillaCookieJar 对象实例来保存cookie
cookiejar = cookielib.MozillaCookieJar(file_name)


# 使用 HTTPCookieProcessor() 创建cookie处理器对象
handler = urllib2.HTTPCookieProcessor(cookiejar)


# 构建opener
opener = urllib2.build_opener(handler)


# 发送请求
response = opener.open("http://www.baidu.com")


# 保存cookie
cookiejar.save()
