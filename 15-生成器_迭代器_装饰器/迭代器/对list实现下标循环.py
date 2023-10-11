#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""对list实现下标循环

Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身
"""
for i,value in enumerate(['A','C','B']):
    print(i,value)


#同时引用两个变量在Py里是很常见的，比如：
for x,y in [(0,1),(1,3),(2,5)]:
    print(x,y)