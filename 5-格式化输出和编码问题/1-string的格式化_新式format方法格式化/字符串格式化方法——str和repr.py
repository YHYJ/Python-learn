#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# repr() ——用来产生一个方便机器解读的字符串形式，输出有特殊作用的字符，比如转译字符\n
# str() ——用来产生一个方便人解读的字符串形式，输出纯字符串
"""对于一个没有可供人方便解读的特殊形式，str()返回值与 repr()返回值相同.

对于数字或者类似于列表和字典的结构，两种方法可以产生同样的表现形式
仅对字符串有两个不同的表现"""
print('*'*50, '字符串')

s = 'Hello,world'
print(str(s))   # 输出Hello,world
print(repr(s))  # 输出'Hello,world'
# 对于许多对象类型，包括大多数内置的，eval（repr（obj））== obj
print(eval(repr(s)))  # 输出Hello,world

h = 'hello,world\n'
print('h = '+h)     # 单纯输出h转义字符起作用
print('str(h) = '+str(h))   # 使用str函数转义字符起作用
print('repr(h) = '+repr(h))     # 使用reor函数将整个h当作一字符串


print('*'*50, '数字')

print(str(1/7))
print(repr(1/7))
x = 10*3.25
y = 200*200
s = 'x的值是' + repr(x) + '，y的值是' + repr(y) + '……'
print(s)
s = 'x的值是' + str(x) + '，y的值是' + str(y) + '……'
print(s)
