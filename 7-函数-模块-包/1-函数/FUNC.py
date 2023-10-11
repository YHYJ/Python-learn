#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""函数就是一个语句块
这块语句有个名字，可以在需要时反复使用这块语句
它有可能需要输入，有可能返回输出"""


# 自建函数
def sayhello():     # 定义函数名sayHello()
    """简单的问候函数"""   # 文档字符串——用来生成有关程序中函数的文档
    print('Say Hello world!')   # 函数内容

if __name__ == '__main__':
    sayhello()
help(sayhello)
