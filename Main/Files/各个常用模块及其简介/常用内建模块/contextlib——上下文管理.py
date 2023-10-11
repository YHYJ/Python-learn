#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们
contextlib 模块提供了3个对象————
装饰器contextmanager、函数nested 和上下文管理器closing
使用这些对象，可以对已有的生成器函数或者对象进行包装-
-加入对上下文管理协议的支持，避免专门编写上下文管理器来支持with语句
"""

from contextlib import contextmanager, closing
from urllib.request import urlopen


# try...finally：
'''正确关闭文件资源的一种方法——繁琐'''
try:
    f = open('./file/hash.txt')
    print(f.read())
finally:
    if f:
        f.close()
'''写try...finally非常繁琐'''


# with
with open('./file/hash.txt') as f:
    file = f.read()
'''open()函数实现了__enter__()和__exit__()方法，因此支持上下文管理协议
支持上下文管理协议的对象都可以使用with调用上下文管理器'''


# 自定义Query()类实现上下文管理器
class Query:
    """自定义上下文管理器支持上下文管理协议"""
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('开始')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('结束')

    def query(self):
        print('Query info about %s...' % self.name)
'''将自定义上下文管理器Query()用于with语句'''
with Query('Bob') as q:
    q.query()
'''编写__enter__()和__exit__()依然繁琐'''


# @contextmanager装饰器
'''contextlib提供的对象'''
class Query_1:
    """借助contextmanager做装饰器改写自定义上下文管理器"""
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query_1 info about %s...' % self.name)

@contextmanager     # @contextmanager装饰器通过编写生成器函数来简化上下文管理
def creat_query(name):
    print('开始')
    q = Query_1(name)
    yield q     # 生成器函数
    print('结束')
'''@contextmanager装饰器接受一个生成器
用yield语句把with...as var变量输出出去'''
with creat_query('Bobly') as q:
    q.query()
'''先执行creat_query()函数的开始两句，第三句遇到yield返回q给with，
执行q.query()打印信息，在执行creat_query()函数最后一句print语句'''


# @closing
'''一个对象不支持上下文协议就无法用于with语句
这时可以用closing()把该对象变为上下文对象。例如：用with语句使用urlopen()'''
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
# closing也是一个经过@contextmanager装饰的generator
'''这个generator编写起来其实非常简单：'''
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
'''它的作用就是把任意对象变为上下文对象，并支持with语句'''