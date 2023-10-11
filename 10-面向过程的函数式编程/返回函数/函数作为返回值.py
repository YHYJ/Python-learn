#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回"""


"""实现一个可变参数的求和"""
# 通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    """求和函数"""
    ax = 0
    for n in args:
        ax += n
    return ax
print(calc_sum(1,2,3,4,5,6))

"""但如果不需要立刻求和，而是在后面的代码中根据需要再计算"""
# 可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum      # 不能加括号，否则返回的是sum函数的返回值，而不是sum函数本身
f = lazy_sum(1,2,3,4,5,6)
print(f)        # 调用lazy_sum()函数时，返回值是求和函数不是求和结果
print(f())      # 只有调用函数f()时才真正计算求和结果

"""注意，当调用lazy_sum()时，每次调用都会返回一个新的函数"""
# 即使传入相同的参数：
f1 = lazy_sum(1,2,3,4,5,6)
print(f == f1)      # 返回值为False

'''函数lazy_sum中又定义了函数sum
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中-
-这种称为“闭包（Closure）”的程序结构拥有极大的威力'''