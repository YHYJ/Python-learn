#!/usr/bin/env python3

import sys
import gc


print("\n垃圾回收机制启动阈值：{}\n".format(gc.get_threshold()))
"""
700：阈值
10：每10次0代垃圾回收，进行一次1代垃圾回收
10：每10次1代垃圾回收，进行一次2代垃圾回收
"""

a = 11
b = a

print("[a]引用计数：{}".format(sys.getrefcount(a)))
print("[b]引用计数：{}\n".format(sys.getrefcount(b)))

print("a = {}".format(a))
print("b = {}\n".format(b))

print("内存地址：")
print("ID[a]：{}\t{}".format(id(a), hex(id(a))))
print("ID[b]：{}\t{}".format(id(b), hex(id(b))))

if id(a) == id(b):
    print("\n内存地址一致\n")
else:
    print("内存地址不同\n")


a = 12123456789
b = 12123456789
A = 'ab'
B = 'ab'
AB = ["very good morning"]
BA = ["very good morning"]
print("a和b指向的对象是否相同：{}".format(a is b))
print("A和B指向的对象是否相同：{}".format(A is B))
print("AB和BA指向的对象是否相同：{}\n".format(AB is BA))
"""
对一个数字或者字符串不同的引用指向同一个对象
列表、元组等数据结构不同引用指向不同地对象，即使指向的值相同
"""

del a
b = 2
print("[a]引用计数：{}\n".format(sys.getrefcount(b)))
print(b)
