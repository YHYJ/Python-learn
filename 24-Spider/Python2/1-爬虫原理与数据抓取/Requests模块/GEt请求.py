#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Requests 继承了urllib2的所有特性：
    Requests支持HTTP连接保持和连接池
    支持使用cookie保持会话
    支持文件上传
    支持自动确定响应内容的编码
    支持国际化的 URL 和 POST 数据自动编码

requests 的底层实现其实就是 urllib3
"""

import requests


url = "http://www.baidu.com"

# 一. 基本GET请求
response_1 = requests.get(url)

# print(response_1.text)


# 二. 添加查询参数和headers
kw = {"wd": "tim"}
headers = {
    "USer-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
response_2 = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
'''params接收字典或字符串类型的查询参数，字典类型自动转换为url编码，不需要urlencode()'''

# print(response_2.text)       # 返回Unicode格式的数据
'''使用response.text时，Requests会基于响应的文本编码自动解码响应内容，大多数Unicode字符集都能被无缝地解码'''
# print(response_2.content)    # 返回字节流数据
'''使用response.content时，返回的是响应数据的原始二进制字节流，可以用来保存图片等二进制文件'''
print(response_2.url)          # 查看完整URL
print(response_2.encoding)     # 查看响应的字符编码
print(response_2.status_code)  # 查看响应状态码
