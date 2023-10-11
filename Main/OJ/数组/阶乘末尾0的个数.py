#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-03-16 00:07:35
Last modified: 2018-03-16 00:07:35
Author: YJ - yj1516268@outlook.com

求n阶乘结果末尾的0的个数，如5! = 120， 0的个数为1
"""


class Solution:
    def trailing2Zeroes(self, n):
        """
        :type n:int
        :rtype:int
        """
        zero = 0
        num = 1
        while n:
            num = num * n
            n -= 1
        snum = str(num)
        for i in snum[::-1]:    # 注意列表的逆置是snum[::-1]
            if i is '0':
                zero += 1
            else:
                break
        return zero


so = Solution()
print(so.trailing2Zeroes(10))
