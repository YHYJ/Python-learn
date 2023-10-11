#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""HTTP格式
每个HTTP请求和响应都遵循相同的格式
HTTP协议是一种文本协议，所以，它的格式也非常简单
一个HTTP包含Header和Body(可选)两部分"""


# HTTP GET请求的格式：
'''
GET /path HTTP/1,1
Header1: Value1
Header2: Value2
Header3: Value3
'''
'''每个Header一行一个，换行符是\r\n'''


# HTTP POST请求格式：
'''
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''
'''当遇到连续两个\r\n时，Header部分结束，后面数据全是Body'''


# HTTP响应格式：
'''
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
'''
'''HTTP响应如果包含body，也是通过\r\n\r\n来分隔的
请再次注意，Body的数据类型由Content-Type头来确定
如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据

当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip
所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩
才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输
'''
