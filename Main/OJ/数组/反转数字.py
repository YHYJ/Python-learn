#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-03-16 00:25:07
Last modified: 2018-03-16 00:25:07
Author: YJ - yj1516268@outlook.com

输入123，输出321；输入-123，输出-321；输入103200，输出2301
"""


class Solution:
    def reverse(self, x):
        """
        :type x:int
        :rtype:int
        """
        if -10 < x < 10:
            return x
        x1 = abs(x)
        y = str(x1)
        v = ''
        for i in range(len(y)):
            v = v + y[-(i + 1)]
        res = int(v)
        if x < 0:
            res = -res
        return res


so = Solution()
print(so.reverse(-1032100))
