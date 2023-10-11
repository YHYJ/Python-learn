#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""装饰器可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便"""

import functools

print("*"*25 + "一、编写一个装饰器，能在函数调用前后都打印日志" + "*"*25)
# 日志信息为：'begin call'和'end call'

def log(func):
    @functools.wraps(func)
    def begin(*args,**kwargs):
        print('begin call:%s' % func.__name__)
        func(*args,**kwargs)
        print('end call:%s' % func.__name__)
    return begin

@log
def hello():
    print('你好色彩！')
hello()


print("*"*25 + "二、写一个@logs工厂装饰器，使它既支持无参又支持有参" + "*"*25)

def logs(text='无参', name='函数名'):     # 设置默认参数，无参调用时使用默认
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s,%s:%s()' % (text, name, func.__name__))
            func(*args,**kwargs)
        return wrapper
    return decorator


@logs()
def not_have():
    print('试验工厂装饰器的无参')


@logs(text='有参')
def have():
    print('试验工厂装饰器的有参')

not_have()
have()
