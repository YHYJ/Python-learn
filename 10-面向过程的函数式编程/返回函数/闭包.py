#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:      # 1
            ax += n
        return ax
    return sum
f = lazy_sum(1,2,3,4,5,6)
print(f)        # 返回f的类型等信息
print(f())      # 返回求和值
'''函数lazy_sum中又定义了函数sum
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中-
-这种称为“闭包（Closure）”的程序结构拥有极大的威力
'''
'''1处 —— 返回的函数sum在内部引用了局部变量args，所以，当一个函数返回了一个函数后-
          -其内部的局部变量可以被内部函数引用
'''
'''另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
'''
# 一个例子：
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)        # 1
    return fs
f1,f2,f3 = count()
'''例子中，每次循环都创建了一个新的f函数，然后把创建的3个函数都返回了
可能认为调用f1()，f2()和f3()结果应该是1，4，9
'''
# 实际结果是：
print('f1 = %d\nf2 = %d\nf3 = %d '%(f1(),f2(),f3()))
'''全都是9
原因就在于返回的函数引用了变量i，但它并非立刻执行
最后返回f函数时，i = 3，count函数1处引用的f的返回值已经变成了9，因此最终结果为9
返回闭包时牢记的一点是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
'''
'''如果返回函数一定要引用循环变量
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值
'''
# 无论循环变量后续如何更改，已绑定到函数参数的值不变：
def count1():
    def f1(j):
        return lambda : j*j   # 因为f1已经传入了参数j，所以lambda函数不需要再给定参数
    fs1 = []
    for i in range(1,4):
        fs1.append(f1(i))    # f1(i)立刻执行，因此i的当前值被传入f1()
    return fs1
F1,F2,F3 = count1()
print('F1 = %d\nF2 = %d\nF3 = %d '%(F1(),F2(),F3()))
'''就是将循环独立出来，在每次循环中调用f1函数进行计算，并将结果加到列表fs中'''

#小结：
# 1、一个函数可以返回一个计算结果，也可以返回一个函数
# 2、返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量