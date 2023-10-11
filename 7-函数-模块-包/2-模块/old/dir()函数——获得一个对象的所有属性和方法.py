#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fibo,sysa


print(dir(fibo))    #查看自定义模块fibo里的方法
print(dir(sys))     #查看模块sys里的方法
a = [1,2]
fibb = fibo.fib
print(dir())    #不加参数dir()会遍历当前定义的变量、模块和函数等


print('*'*100)

'''dir()无法遍历内置的函数和变量的名称.

但在标准模块builtins中定义有一个这样的列表
'''
import builtins
print(dir(builtins))


print('*'*100)

print(dir('ABC'))
'''类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度
在Py中，如果调用len()函数试图获取一个对象的长度，实际上，在len()函数内部-
-它自动去调用该对象的__len__()方法
'''
# 所以，下面的代码是等价的：
print(len('ABC'))
print('ABC'.__len__())


"""仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()"""
# 可以直接操作一个对象的状态：
class MyObject():

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print('*'*25,'获取属性','*'*25)

print(hasattr(obj,'x'))     # 有属性‘x’么
print(getattr(obj,'x'),obj.x)     # 获取属性‘x’
print(hasattr(obj,'y'))     # 有属性‘y’么
setattr(obj,'y',16)         # 设置一个属性‘y’
print(getattr(obj,'y'),obj.y)     # 获取属性‘y’
print(getattr(obj,'z',404))     # 获取属性‘z’，如果不存在，返回默认值404

print('*'*25,'获取方法','*'*25)

print(hasattr(obj,'power'))     # 有属性‘power’么
print(getattr(obj,'power'))
fn = getattr(obj,'power')
print(fn)
print(fn())