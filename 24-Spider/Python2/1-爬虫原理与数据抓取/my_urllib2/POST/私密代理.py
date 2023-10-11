#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import urllib2

from conf.User_Agent_list import USER_AGENT_LIST


# 构建两个代理Handler，一个有代理IP一个没有
# httpproxy_handler = urllib2.ProxyHandler({"http": "31.47.198.61:80"})     # 免费代理
httpproxy_handler = urllib2.ProxyHandler({"http": "mr_mao_hacker:sffqry9r@120.27.218.32:16816"})   # 私密代理
nullproxy_handler = urllib2.ProxyHandler({})

proxySwitch = True  # 代理开关


# 调用 build_opener() 方法创建支持HTTP代理的opener对象
if proxySwitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)


# 构建 Request 请求
url = "http://www.baidu.com/"
headers = {"User-Agent": random.choice(USER_AGENT_LIST)}

request = urllib2.Request(url, headers=headers)


response = opener.open(request)


print response.read()
