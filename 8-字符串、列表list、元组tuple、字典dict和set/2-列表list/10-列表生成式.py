#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""列表生成式将for循环和创建新元素的代码合并为一行，自动追加新元素
把要生成的元素x*x放到前面，后面跟for循环"""


# 一、普通列表生成式
print("*"*25 + "一、普通列表生成式" + "*"*25)
'''列表生成式创建[1x1, 2x2, 3x3, ..., 10x10]列表'''
squares = [num*num for num in range(1, 11)]
print(squares)
'''在for循环后加if判断进行目的性筛选——筛选出仅偶数的平方'''
duo_number = [num**2 for num in range(1, 11) if num % 2 == 0]
print(duo_number)
'''使用两层循环生成’ABC‘和’XYZ‘的全组合'''
mn = [m+n for m in 'ABC' for n in 'XYZ']
print(mn)
'''同时使用两个甚至多个变量来生成list'''
dictionary = {'x轴': 15, 'y轴': 18, 'z轴': 20}
di_list = ['%s=%s' % (k, str(v)) for k, v in dictionary.items()]
print(di_list)
'''把一个list中所有的字符串变成小写并去除数字'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l, str) is True]   # 内建isinstance函数判断一个变量是不是字符串
print(L2)


# 二、嵌套列表生成式
print("*"*25 + "二、嵌套列表生成式" + "*"*25)
'''用长度为 4 的 3 个列表实现的 3*4 维的矩阵'''
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]
]
matrix_2 = [[row[i] for row in matrix] for i in range(4)]   # 对matrix中的元素的行列坐标进行对调
print('3*4维矩阵：%s' % matrix_2)
'''等同于'''
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
'''路径：最外层for循环分别是0, １，２，３
为0时，通过内层for循环挨次取出matrix每个元素（其元素为列表）中的第0个元素添加到matrix（或transposed）
'''
