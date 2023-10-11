#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""WSGI：Web Server Gateway Interface
它只要求Web开发者实现一个函数，就可以响应HTTP请求"""


"""静态HTML
最简单的Web应用就是先把HTML用文件保存好
用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回
Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的"""


"""动态HTML
动态HTML需要把上述步骤自己实现
接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活
如果自己来写这些底层代码，还没开始写动态HTML，就得花个把月去读HTTP规范
正确的做法是底层代码由专门的服务器软件实现，Py专注于生成HTML文档
因为不希望接触到TCP连接、HTTP原始请求和响应格式
所以需要一个统一的接口，让web开发者专心用Py编写Web业务"""


"""这个接口就是WSGI：Web Server Gateway Interface
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求"""


# 最简单的Web版本的“Hello, web!”：
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello web!</h1>']
'''
application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
    environ：一个包含所有HTTP请求信息的dict对象
    start_response：一个发送HTTP响应的函数
在application()函数中，调用：
    start_response('200 OK', [('Content-Type', 'text/html')])
就发送了HTTP响应的Header，Header只能发送一次，也就是只能调用一次start_response()函数
start_response()函数接收两个参数：
    HTTP响应码
    一组list表示的HTTP Header，每个Header是一个tuple，包含两个str

通常情况下，都应该把Content-Type头发送给浏览器
其他很多常用的HTTP Header也应该发送
然后函数的返回值将作为HTTP响应的Body发送给浏览器
'''


"""有了WSGI，开发者关心的就是
如何从environ这个dict对象拿到HTTP请求信息
然后构造HTML，通过start_response()发送Header，最后返回Body"""


"""
整个application()函数本身没有涉及到任何解析HTTP的部分
也就是说底层代码不需要自己编写，开发者只负责在更高层次上考虑如何响应请求就可以

application()函数必须由WSGI服务器来调用
有很多符合WSGI规范的服务器，可以挑选一个来用

Py内置了一个WSGI服务器，这个模块叫wsgiref
它是用纯Py编写的WSGI服务器的参考实现
所谓“参考实现”是指该实现完全符合WSGI标准
但是不考虑任何运行效率，仅供开发和测试使用
"""
