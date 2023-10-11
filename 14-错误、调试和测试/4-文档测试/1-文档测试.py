#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""写在注释中的代码可以自动执行"""

"""Py内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
doctest严格按照Py交互式命令行的输入和输出来判断测试结果是否正确
只有测试异常的时候，可以用...表示中间一大段烦人的输出"""

# 用doctest测试自定义的Dict类 ——>mydict.py

# work:对函数fact(n)编写doctest ——> work.py