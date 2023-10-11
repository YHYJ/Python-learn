# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""contextlib 模块提供了3个对象：
装饰器contextmanager、函数nested 和上下文管理器closing
使用这些对象，可以对已有的生成器函数或者对象进行包装-
-加入对上下文管理协议的支持，避免专门编写上下文管理器来支持with语句
"""


from contextlib import contextmanager
