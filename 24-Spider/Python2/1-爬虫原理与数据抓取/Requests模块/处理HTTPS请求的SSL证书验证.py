#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


# response = requests.get("https://www.12306.cn/mormhweb/", verify=True)  # 检查主机SSL证书
response = requests.get("https://www.12306.cn/mormhweb/", verify=False)    # 不检查SSl证书

print(response.content)
