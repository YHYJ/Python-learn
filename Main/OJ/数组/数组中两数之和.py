#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-03-13 15:14:18
Last modified: 2018-03-13 15:14:18
Author: YJ - yj1516268@outlook.com

在一个整数数组中找到两个数使得他们的和等于一个给定的数target
按顺序返回这两个数的下标，注意这里下标的范围是1到n，不是以0开头
"""


class My:
    """加法
    两数之和：target
    """
    def twosum(self, nums, target):
        for i, j in enumerate(nums[:]):
            for x, y in enumerate(nums[1:]):
                if j + y == target:
                    return [i + 1, x + 2]


my = My()
print(my.twosum([7, 2, 15, 11], 9))


class Other:
    """减法
    两数之和：target
    """
    def twosum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index

        for i, v in enumerate(nums):
            if target - v in hash_map:
                i_2 = hash_map[target - v]
                if i != i_2:
                    return [i+1, i_2 + 1]


other = Other()
print(other.twosum([7, 2, 15, 11], 9))
