#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

__author__ = '1516 YJ'      # __author__变量接收开发者姓名

import sys

def test():
    args = sys.argv     # argv将命令行中给定的参数存储到列表，它的第一个元素永远是该.py文件本身
    if len(args) == 1:  # args只有一个元素时
        print('Hello,world!')
    elif len(args) == 2:    # args有两个元素时
        print('Hello,%s!' % args[1])    # 打印下标为1的元素
    else:
        print('Too many arguements!')

if __name__ == '__main__':
    test()

'''当在命令行运行hello.py时，Py解释器把一个特殊变量__name__置为__main__
而在其他地方导入该hello模块时,if判断将失败
因此这种if测试可以让一个模块通过命令行运行时执行一些额外的代码,最常见的就是运行测试
'''