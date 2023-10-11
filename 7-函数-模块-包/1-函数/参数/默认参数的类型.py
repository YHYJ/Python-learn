#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""重要提醒： 默认值仅被设置一次，这与以前默认值为可变对象（如列表、字典和多数类实
例时）有很大的区别。例如， 接下来的方法累计被传入的参数变量到下次调用.
"""

# 默认参数不能是可变类型，否则会保存之前的数据
def f(a, l=[]):
    l.append(a)
    return l
print(f(1))
print(f(a=12, l=[123]))
print(f(2))     # 每调用一次，l[]在原有元素后添加


def f1(a, num_list=None):
    """
    不指定num_list类型的话，默认是list类型
    """
    if num_list is None:
        num_list = []
    num_list.append(a)
    return num_list
print(f1(123))  # 每调用一次，l[]不是在原有元素后添加
print(f1(456))


def parrot(voltage, state='a stiff', action='voom', ty='Norwegian Blue'):
    print("-- This parrot wouldn’t", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", ty)
    print("-- It’s", state, "!\n")
parrot(1000)
parrot(1000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('大', '中', ty='小')
parrot(233333, action='66666')
parrot(voltage=5.0, state='dead')
