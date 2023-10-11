#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-21 17:40:50
Last modified: 2017-09-21 17:40:50
Python release: 3.6.2

iter()函数获得可迭代对象的迭代器，实际是调用了可迭代对象的__iter__()方法
next()函数获取迭代器的下一个数据
"""


li = [0, 1, 2, 3, 4, 5, 6]

li_iter = iter(li)

print(li)
print(li_iter)
print('0 + ', next(li_iter))
print('1 + ', next(li_iter))
print('2 + ', next(li_iter))
print('3 + ', next(li_iter))
print('4 + ', next(li_iter))
print('5 + ', next(li_iter))
print('6 + ', next(li_iter))
# print('7 + ', next(li_iter))
'''迭代完最后一个元素时，再次调用next()函数会抛出StopIteration异常'''
