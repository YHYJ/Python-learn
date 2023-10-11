#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""操作系统提供的命令只是简单地调用了操作系统提供的接口函数
Py内置的os模块也可以直接调用操作系统提供的接口函数"""


import os

print(os.name)      # 'posix'代表linux、unix或者OS x，'nt'代表windows
print(os.uname())   # 获取详细的系统信息


"""环境变量：
在操作系统中定义的环境变量全部保存在os.environ这个变量中"""
# 可以直接查看：
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
