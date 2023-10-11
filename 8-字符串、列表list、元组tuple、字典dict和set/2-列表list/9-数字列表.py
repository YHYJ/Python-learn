#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用函数list()将range()的结果转换为列表
对数字列表进行简单的统计计算
work
"""


# 使用函数list()将range()的结果转换为列表
print('*'*25 + '一、使用函数list()将range()的结果转换为列表' + "*"*25)
i = range(1, 6)              # 不经过list转换输出i的值为range(1,5)
print(type(i), i)
i = list(range(1, 6))                 # 经过list转换，输出列表
print(i)

num = list(range(2, 11, 2))   # 指定range()步长打印1~11之间的偶数
print(num)

nums = []
for i in range(1, 11):       # 创建包含1~10间整数的平方的列表
    nums.insert(0, i**2)     # 倒序置入到空列表nums
print(nums)


# 对数字列表进行简单的统计计算
print('*'*25 + '二、对数字列表进行简单的统计计算' + "*"*25)
number = [-1314, -10, -9, -8, -7, 4, 5, 6, 7, 8, 9, 10, 1516, ]
print(min(number))  # 最小值
print(max(number))  # 最大值
print(sum(number))  # 总和


# work
print('*'*25 + 'work' + "*"*25)
# 打印1~20奇数列表
odd_num = [i for i in list(range(1, 20, 2))]
print(odd_num)
# 打印3~30能被3整除的数字的列表
three_num = [i for i in list(range(3, 31, 3))]
print(three_num)
# 打印1~10整数的立方的列表
CU_num = [i ** 3 for i in list(range(1, 11))]
print(CU_num)
