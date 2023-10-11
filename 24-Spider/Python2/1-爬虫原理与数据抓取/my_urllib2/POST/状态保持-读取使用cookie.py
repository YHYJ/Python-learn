#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib2
import cookielib


# 创建MozillaCookieJar实例对象
cookiejar = cookielib.MozillaCookieJar()

# 从文件读取cookie
cookie = cookiejar.load("cookie")

# 使用HTTPCookieProcessor()创建cookie处理器对象
handler = urllib2.HTTPCookieProcessor(cookiejar)

# 构建opener
opener = urllib2.build_opener(handler)


response = opener.open("http://www.baidu.com")


print(response.read())