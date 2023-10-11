#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
递推式构造列表提供了一些简洁的方法来创建列表
其中的元素是对其他序列或迭代上每个元素操作后的结果
或者在原序列基础上创建一个其中元素满足特定条件的子序列
"""

from math import pi


square = []
for i in range(10):
    square.append(i ** 2)
print(square)
# 简写为：
squares = [x**2 for x in range(10)]
print(squares)


# 结合两个列表不相等的元素
l = [(x, y) for x in [1, 2, 8, 4] for y in [3, 1, 4] if x !=y]
print(l)
# 等同于：
li = []
for x in [1, 2, 8, 4]:
    for y in [3, 1, 4]:
        if x != y:
            li.append((x, y))
print(li)

print('*'*100)


vec = [-3, -2, -1, 0, 1, 2, 3, ]     # 创建一个 0 为轴左右对称的列表
print([x*2 for x in vec])            # 对列表 vec 的每个元素翻倍
print([x for x in vec if x >= 0])    # 过滤列表 vec 中的负数
print([abs(x) for x in vec])         # 对列表 vec 的元素调用abs方法求绝对值

print('*'*100)


# 为每个元素调用方法去掉元素中首尾空格
freshfruit = [' banana ', ' loganberry ', ' passion fruit ']
print([weapon.strip() for weapon in freshfruit])

print('*'*100)

# 创建一个包含二维数组的列表，数组数据必须用括号括起来
print([(x, x**2) for x in range(6)])

print('*'*100)


# 用两个 for 遍历展开所有的列表元素,并进行排序
vec = [[1, 3, 2], [4, 6, 5], [7, 9, 8]]
print(sorted([num for elem in vec for num in elem]))

print('*'*100)


print([str(round(pi, i))for i in range(1, 6)])
print(round(pi, 1))
print(round(121.6, -1))
'''round 内建函数
第一个参数是一个10进制的数，第二个参数是对第一个参数进行四舍五入的精度
第二个参数为负数代表对整数部分进行四舍五入
正数为对小数部分进行四舍五入，数值代表精度，默认值为0
'''
