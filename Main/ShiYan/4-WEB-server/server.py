#!/usr/bin/env python3

"""探索 HTTP 协议和 Web 服务的基本原理
同时学习 Py 如何实现 Web 服务请求、响应、错误处理及CGI协议
最后根据项目需求使用 Py 面向对象思路对代码进行重构
知识点：
    HTTP 协议基本原理
    简单的 Web 服务器框架
    Python 语言的网络开发
    Web 服务请求，响应及错误处理的实现
    CGI 协议的 Python 实现
    使用 Python 面向对象思想重构代码
"""

"""web服务器基本概念：
    1、等待浏览器连接服务器并发送一个HTTP请求
    2、解析该请求
    3、了解该请求希望请求的内容
    4、服务器根据请求抓取需要的数据（从服务器本地文件中读或者程序动态生成）
    5、将数据格式化为请求需要的格式
    6、送回HTTP响应
"""

