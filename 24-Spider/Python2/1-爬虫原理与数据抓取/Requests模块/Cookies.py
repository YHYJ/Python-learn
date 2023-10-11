#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


url = "http://www.baidu.com/"

"""拿到响应中的Cookies"""
response = requests.get(url)

# 返回CookieJar对象
cookiejar = response.cookies

# 转换CookieJar为字典
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)


print(cookiejar)
print(cookiedict)
