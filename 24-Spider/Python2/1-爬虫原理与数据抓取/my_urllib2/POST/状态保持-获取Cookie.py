#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""cookielib库和HTTPCookieProcessor处理器
在Python处理Cookie，一般是通过cookielib模块和urllib2模块的HTTPCookieProcessor处理器类一起使用
    cookielib模块：主要作用是提供用于存储cookie的对象
        该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar
            1. CookieJar：
               管理HTTP cookie值、存储HTTP请求生成的cookie、向传出的HTTP请求添加cookie的对象
               整个cookie都存储在内存中，对CookieJar实例进行垃圾回收后cookie也将丢失。
            2. FileCookieJar (filename,delayload=None,policy=None)：
               从CookieJar派生而来，用来创建FileCookieJar实例，检索cookie信息并将cookie存储到文件中
               filename是存储cookie的文件名，
               delayload为True时支持延迟访问访问文件，即只有在需要时才读取文件或在文件中存储数据
            3. MozillaCookieJar (filename,delayload=None,policy=None)：
               从FileCookieJar派生而来，创建与Mozilla浏览器 cookies.txt兼容的FileCookieJar实例
            4. LWPCookieJar (filename,delayload=None,policy=None)：
               从FileCookieJar派生而来，创建与libwww-perl标准的 Set-Cookie3 文件格式兼容的FileCookieJar实例
        大多数情况下只用CookieJar()，如果需要和本地文件交互，就用 MozillaCookjar() 或 LWPCookieJar()

    HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象
"""

import urllib2
import cookielib


# 1. 获取Cookie，保存到 CookieJar 对象中
"""构建一个 CookieJar 对象实例以保存cookie"""
cookiejar = cookielib.CookieJar()

"""使用 HTTPCookieProcessor() 创建cookie处理器对象，参数是 CookieJar() 对象"""
hangler = urllib2.HTTPCookieProcessor(cookiejar)

"""通过 build_opener() 构建opener"""
opener = urllib2.build_opener(hangler)

"""以 GET 方法访问页面，访问之后会自动保存cookie到 cookiejar 中"""
opener.open("http://www.baidu.com")

"""按照标准格式将保存的Cookie打印出来"""
cookieStr = ""
for item in cookiejar:
    cookieStr = "{}{}={};".format(cookieStr, item.name, item.value)

print(cookieStr[:-1])

