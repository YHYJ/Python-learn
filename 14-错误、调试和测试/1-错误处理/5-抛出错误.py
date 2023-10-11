#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""因为错误是class，捕获一个错误就是捕获到该class的一个实例
因此错误并不是凭空产生，而是有意创建并抛出的
Py的内置函数会抛出很多类型的错误，自己编写的函数也可以抛出错误"""

"""如果要抛出错误，首先可以根据需要定义一个错误的class，选择好继承关系"""
# 然后用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# foo('0')
'''只有在必要的时候才定义自己的错误类型
如果可以选择Py内置的错误类型（比如ValueError，TypeError）
尽量使用Py内置的错误类型'''


"""一种常见的错误抛出方式"""
def func(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        func('0')
    except ValueError as error:
        print('ValueError!')
        raise

# bar()
'''bar()函数已经捕获了错误，但打印一个ValueError!后，又把错误通过raise语句抛出
这种错误处理方式相当常见 ——
    捕获错误目的只是记录一下，便于后续追踪
    但由于当前函数不知道应该怎么处理该错误
    所以最恰当的方式是继续往上抛，让顶层调用者去处理
raise语句如果不带参数，就会把当前错误原样抛出'''
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
'''只要合理的转换逻辑就可以，但决不应该把一个IOError转换成毫不相干的ValueError'''