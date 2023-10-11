#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl    # 1. 导入Python的SSL处理模块
import random
import urllib
import urllib2

from conf.User_Agent_list import USER_AGENT_LIST


# 2. 忽略未经认证的SSL证书
context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"
headers = {"User-Agent": random.choice(USER_AGENT_LIST)}

request = urllib2.Request(url, headers=headers)

# 3. 在urlopen()方法里添加 context 参数
response = urllib2.urlopen(request, context=context)

print response.read()
