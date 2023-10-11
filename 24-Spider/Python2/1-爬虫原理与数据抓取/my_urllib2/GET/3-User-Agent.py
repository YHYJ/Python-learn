#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""设置User-Agent以伪装成浏览器"""

import urllib2


url = "http://yj1516.site"

# Chrome 59.9
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/59.0.3071.86 Safari/537.36"
}

# 构造Request请求，伪装成Chrome 59.9
request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request)

html = response.read()

# print html
