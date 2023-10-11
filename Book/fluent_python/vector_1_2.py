#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-03-19 11:00:11

__repr__、__abs__、__add__、__mul__
"""

from math import hypot


class Vector:
    """操作向量. """

    def __init__(self, x=0, y=0):
        """TODO: to be defined1.

        :x: float
        :y: float

        """
        self.x = x
        self.y = y

    def __repr__(self):
        """Python内置函数repr的底层，返回参数的规范字符串表示形式.
        :returns: str: 'Vector(*, *)'

        """
        return "Vector({}, {})".format(self.x, self.y)

    def __abs__(self):
        """返回参数的绝对值/模.
        参数是整数/浮点数返回其绝对值，是复数返回其模
        :returns: float

        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """返回参数的绝对值/模的bool值.
        :returns: bool: True/False

        """
        # return bool(abs(self))  # 常规：耗时（abs->__abs__->平方->开方）
        return bool(self.x or self.y)   # 高效

    def __add__(self, other):
        """+运算符.

        :other: str: 'Vector(*, *)'
        :returns: str: 'Vector(*, *)'

        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """*运算符.

        :scalar: float: 乘数
        :returns: Vector

        """
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 3)  # 向量v1
v2 = Vector(1, 1)  # 向量v2
v = v1 + v2  # 向量的加法
vx = v1 * 3  # 向量的标量乘法
print('v = {}'.format(v))
print('vx = {}'.format(vx))
print('v的模 = {}'.format(abs(v)))  # 向量的模
print('v的布尔值 = {}'.format(bool(v)))  # 向量模的bool值
