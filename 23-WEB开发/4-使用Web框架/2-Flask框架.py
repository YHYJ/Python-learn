#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""使用flask框架处理URL"""


# 写一个app.py，处理3个URL，分别是：——>./package/app.py
'''
GET / ：首页，返回Home
GET /signin ：登录页，显示登录表单
POST /signin ：处理登录表单，显示登录结果
同一个URL /signin分别有GET和POST两种请求，映射到两个处理函数中

Flask通过装饰器在内部自动把URL和函数关联起来
'''
