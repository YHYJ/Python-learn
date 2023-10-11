#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在队列中元素是 ”先进先出“ 顺序
列表当作队列用效率不是很高
因为尽管在列表末增删元素很快，但是在列表开头增删元素很慢
因为所有元素都要改变下标
为了实现队列，可以用 collections.deque 方法，它可以从两端进行快速的增删
"""


from collections import deque
queue = deque(['1', '2', '3'])
print(queue)
queue.append('4')
queue.append('5')
print(queue)
queue.popleft()     # 删除第1个元素
print(queue)        # 按照增加顺序排列剩余队列
queue.popleft()     # 删除第2个元素
print(queue)        # 按照增加顺序排列剩余队列
