#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
栈中的元素是 ”后进先出“ 顺序
列表的方法很容易实现把列表当作栈使用
给栈添加单个元素可以用方法 append() 
从栈顶检索一个元素用不带参数方法 pop()
"""


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())  # 检索元素 '7' 并删除
print(stack)    # stack = [3,4,5,6]
