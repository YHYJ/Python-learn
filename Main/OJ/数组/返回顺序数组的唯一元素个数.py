#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-03-13 13:22:40
Last modified: 2018-03-13 13:22:40
Author: YJ - yj1516268@outlook.com

题目：从一个有序数组中去除重复的数字，返回处理后的数组长度
要求：不使用额外的数组，只能用常量
"""


class Solution:
    """
    遍历数组，跳过重复元素，用不重复元素替换被比较元素后的第一个重复元素
    时间复杂度O(n)
    只适合有序数组
    """
    def rmDuplicates(self, A):
        if len(A) <= 1:
            return len(A)

        index = 0
        for i in A[1:]:     # i：被比较元素
            if i != A[index]:
                index += 1      # 下一个元素
                A[index] = i    # 将下个不重复元素前移到上个不重复元素后

        return index + 1


so = Solution()
print(so.rmDuplicates([]))
print(so.rmDuplicates([1]))
print(so.rmDuplicates([0, 1, 1, 1, 2, 3, 3]))
