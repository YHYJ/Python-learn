#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""一个Web App就是写一个WSGI的处理函数，针对每个HTTP请求进行响应
但是问题是如何处理100个不同的URL
每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求
但是通常只考虑最常见的GET和POST请求"""


"""需要在WSGI接口之上进一步抽象，让开发者专注于用一个函数处理一个URL
至于URL到函数的映射，就交给Web框架来做"""
