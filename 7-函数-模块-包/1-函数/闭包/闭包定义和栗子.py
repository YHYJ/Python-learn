#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-01-04 17:54:13
Last modified: 2018-01-04 17:54:13
Author: YJ1516 - yj1516268@outlook.com

闭包：一种程序结构，由<函数>和<自由变量>组成，该函数引用该自由变量
形似：
    def func_o(*arg):
        def func_i():
            use arg
        return func_i
func_o()函数返回函数func_i本身（而非它的执行结果）
当返回该函数时，相关外部参数和变量的引用都保存在返回的函数中，由此形成一个闭包
"""


def adder(x):
    def wrapper(y):
        return x*2 + y
    return wrapper      # 返回内部函数wrapper


adder1 = adder(5)       # 闭包 adder1 ，包含自由变量 x
print(adder1(10))


def count():
    """返回函数不要引用任何循环变量，或者后续会发生变化的变量
    为什么最后值是三个4：
    调用count()函数时候，执行其内部代码
    此时i=0——
    但注意，因为没有调用f()函数，它不执行，只是将该函数本身存到列表fs
    当i=2、i=3时情况一样
    最后i=3，返回fs列表，其中3个元素保存的是i的外部引用
    使用f1、f2、f3接收返回值，当执行f1、f2、f3时候，将i的引用当做参数传递
    此时i=2，因此最后结果是3个4
    和上面的闭包adder类似
    """
    fs = []
    for i in range(3):
        def f():
            return i*i
        fs.append(f)        # 将内部函数 f 存到fs列表
    return fs               # 返回列表fs


f1, f2, f3 = count()        # 三个闭包，包含自由变量 i
print(f1(), f2(), f3())     # 执行内部函数，因为调用 count() 时候i的值已经是2，所以结果为9

fff = count()
for i in fff:
    print(i())
