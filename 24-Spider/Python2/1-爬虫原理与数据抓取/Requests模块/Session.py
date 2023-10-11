#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""登录人人网"""

import requests


# 1. 创建session对象以保持Cookie值
session = requests.session()

# 2. headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 3. 登录信息
user_pwd = {
    "email": "mr_mao_hacker@163.com",
    "password": "alarmchime"
}

# 4. 发送一次请求，获取Cookie，保存到session里
session.post("http://www.renren.com/PLogin.do", data=user_pwd)

# 5. 访问
response = session.get("http://www.renren.com/410043129/profile")

# 6. 响应内容
print(response.content)
