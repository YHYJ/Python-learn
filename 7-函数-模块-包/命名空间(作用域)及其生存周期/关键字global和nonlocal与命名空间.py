#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


# global关键字
'''用来在函数或其他局部作用域中修改全局变量
如果只调用不修改全局变量也可以不使用global关键字'''
info = 0

def info_test():
    print(info)
info_test()     # 不修改全局变量也可以不使用global关键字

def info_counter():
    global info
    info += 1
    return info
print(info_counter())


# nonlocal关键字
'''用来在函数或其他作用域中使用外层(非全局)变量'''
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 2
        return count
    return counter

def make_counter_test():
    mc = make_counter()
    print(mc())
    print(mc())

make_counter_test()
