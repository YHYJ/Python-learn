#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-23 17:18:49
Last modified: 2017-09-23 17:18:49
Python release: 3.6.2

生成器函数执行到yield语句时会保存当前运行状态（断点），然后暂停执行，即将生成器函数挂起
next()函数可以唤醒生成器函数，除此之外send()函数也可以唤醒生成器函数
"""


def go():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

g = go()

print(next(g))
print()
print(next(g))
print()
print(next(g))
print()'''
print(g.send('接下来'))
'''
i = 0，yield 0并打印，并不赋值给temp，next()唤醒go函数继续执行，
执行到print(temp)语句，temp值为None
i = 0，yield 1并打印，并不赋值给temp，next()唤醒go函数继续执行，
执行到print(temp)语句，temp值为None

next temp一直是None
send 可以指定temp的值
'''
