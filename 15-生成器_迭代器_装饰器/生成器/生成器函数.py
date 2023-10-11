#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""生成器函数的定义：
一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数-
-而是一个生成器函数
"""


# 将斐波那契数列用生成器函数打印出来：
def fibonacci_series(max):
    """生成器函数打印斐波那契数列"""
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b     # 生成器实际上定义算法，可以从第一个元素开始推算出后续任意元素
        n += 1
    return None

fib = fibonacci_series(6)
    # fib.close()
print(fib)       # 输出显示生成了<generator...>生成器
# for f in fib:   # 用for循环调用生成器函数拿不到函数的return语句的返回值
#    print(f)
while True:
    try:
        x = next(fib)
        print('fib:',x)
    except StopIteration as val:        # 想要拿到返回值，必须捕获StopIteration错误
        print('生成器返回：',val.value)   # 返回值包含在StopIteration的value中
        break

"""生成器函数和普通函数的执行流程不一样

普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回
生成器函数在每次调用next()时执行，遇到yield语句返回-
-再次执行时从上次返回的yield语句处继续执行
"""


print("*"*25 + "work" + "*"*25)

# 将杨辉三角用生成器函数打印出来：
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]

n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break

