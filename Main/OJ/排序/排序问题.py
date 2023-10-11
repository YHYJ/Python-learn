#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Date: 2018-03-15 23:41:23
Last modified: 2018-03-15 23:41:23
Author: 王斌 - yj1516268@outlook.com

合并两个递增数组，合并后的数组依旧递增
"""


class Solution:
    def merge(self, nums1, nums2):
        """
        :type nums1:List[int]
        :type m:int
        :type nums2:List[int]
        :type n:int
        :rtype: vido Do not return anything,modify nums1 in-place instead
        """
        nums1 = nums1 + nums2
        nums1.sort()
        return nums1

    def merge_1(self, nums1, nums2):
        nums1 = nums1 + nums2
        for x in range(len(nums1)-1):
            for y in range(x + 1, len(nums1)):
                if nums1[y] < nums1[x]:
                    nums1[x], nums1[y] = nums1[y], nums1[x]
        return nums1


so = Solution()
print(so.merge(nums1=[1, 3, 5], nums2=[2, 4, 6]))
print(so.merge_1(nums1=[1, 3, 5], nums2=[2, 4, 6]))
