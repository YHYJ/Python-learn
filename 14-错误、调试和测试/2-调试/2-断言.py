#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""凡是用print()来辅助查看的地方，都可以用断言（assert）替代"""


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'   # 意思是：表达式n != 0应该是True，否则后面代码会出错
    print(10/n)
    # return 10 / n


if __name__ == "__main__":
    foo(0)
'''断言失败assert语句本身会抛出AssertionError，并跟着assert语句后的错误提示：n is zero'''
'''启动Py解释器时可以用-O参数关闭assert'''
