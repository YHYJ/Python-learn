#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""定义完整的装饰器函数
不需要编写wrapper.__name__ = func.__name__
Py内置的functools.wraps效力于此
只需在定义wrapper()前加上 @functools.wraps(func) 即可
"""


import functools

def log(func):
    """无参数的装饰器"""
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('func name：%s()' % func.__name__)
        func(*args,**kwargs)
    return wrapper



def logs(text):
    """有参数的装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s：%s()' % (text,func.__name__, ))
            func(*args,**kwargs)
        return wrapper
    return decorator


@log
def date():
    print('2017-6-7')

@logs('函数名')
def time():
    print('16:23')

if __name__ == '__main__':
    date()
    time()

