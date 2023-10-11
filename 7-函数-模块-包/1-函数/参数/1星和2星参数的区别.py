#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# *arg 和 **arg：
# 1. *arg 和 **arg 可以不传递参数
# 2. *arg 将参数转换为元组，**arg将参数转换为字典
# 3. 先处理 arg 参数，再处理 *arg 参数，最后处理 **arg 参数
# 4. 所以，实参先将对应参数传递给形参的 arg 参数，再将对应参数传递给 *arg 参数，而 **arg 参数取得形如 a = xx 有赋值的参数
def test(a, b, *A, **B):
    print(a, b, A, B)
test(1, 2,
     3, (4, 5), [6, 7], {'A': 8, 'B': 9}, ([10, 11, 12]),
     c=13, d=(14, 15), e=[16, 17], f={'C': 18, 'D': 19}, g=([20, 21]))
# 如上，1，2传递到 arg 参数a，b，其余直到c = xx部分前传递到 *arg 参数，而从 c = 13 开始形如 a = xx 的传递到 **arg 参数

''' *arg 和 **arg 参数
*name  接受包含位置参数的元组
**name 接受所有关键字参数组成的字典
两者结合使用，*name 必须在**name 之前.
'''
def cheeseshop(kind, *arguments, **keywords):
    print("你有" + kind + '么？')
    print("我没有" + kind)
    print(arguments)
    for arg in arguments:
        print(arg)
    print("-"*40)
    mmp = sorted(keywords.keys())      # 对字典按照键进行排序
    for kw in mmp:
        print(kw + ":" + str(keywords[kw]))
cheeseshop('橡皮', '一二三', '四五六', a=123, c=789, b=456)
