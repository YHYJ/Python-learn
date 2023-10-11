#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''可迭代对象（Iterable）的定义.

可以直接作用于 for 循环的对象.
'''
#可直接作用于for的数据类型有：
# 一、集合数据类型：list、tuple、dict、set、str
# 二、generator：即生成器和带　yiled 的生成器函数


#可以使用collections模块的isinstance()判断一个对象是否是可迭代对象：
from collections import Iterable

print(isinstance([1,2,3],Iterable))     # 列表list可迭代
print(isinstance({'a': 1,},Iterable))   # 字典dict可迭代
print(isinstance({1,2,3},Iterable))     # 集合set可迭代
print(isinstance((1,2,3),Iterable))     # 元组tuple可迭代
print(isinstance('abc',Iterable))       # 字符串str可迭代
print(isinstance(100,Iterable))         # 数字不可迭代
print(isinstance((x for x in range(1,10)),Iterable))    # 生成器是可迭代对象


'''可迭代对象要求支持迭代器协议.

在Python中，支持迭代器协议就是指可以实现对象的iter()和next()方法.
iter()方法返回迭代器对象本身,对于可迭代对象可以获取它的迭代器对象
next()方法返回容器中的下一个元素,最后引发StopIteration异常
'''