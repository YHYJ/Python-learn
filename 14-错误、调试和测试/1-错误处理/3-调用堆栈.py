#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""错误没有被捕获就会一直往上抛，最终被Py解释器捕获，打印错误堆栈和信息，然后程序退出"""

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

'''解读错误信息是定位错误的关键
从上往下可以看到整个错误的调用函数链，错误信息最后一行提示错误的源头'''