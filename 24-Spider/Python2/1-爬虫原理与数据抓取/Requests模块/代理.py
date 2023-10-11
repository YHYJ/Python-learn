#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


url = "http://www.baidu.com"
proxies = {"http": "http://12.34.56.79:9527"}

response = requests.get(url, proxies=proxies)

print("content：{}".format(response.content))
