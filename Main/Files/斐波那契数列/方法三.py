#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-23 15:55:18
Last modified: 2017-09-23 15:55:18
Python release: 3.6.2

自定义迭代器实现斐波那契数列
"""


class Fib(object):
    """斐波那契数列迭代器"""
    def __init__(self, max):
        """
        :param max: 指定生成数列的前max个数
        """
        self.max = max
        self.value = 0  # 记录生成了数列中的第几个数了
        self.x = 0      # 保存向前数第二位数，初始值为数列第一个数0
        self.y = 1      # 保存前一位数，初始值为数列第二个数1

    def __next__(self):
        """
        next()函数调用来获取下一个数
        """
        if self.value < self.max:
            num = self.y
            self.x, self.y = self.y, self.x + self.y
            self.value += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    fib = Fib(max = 5)
    for i in fib:
        print(i)
