#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""如果不捕获错误，自然可以让Py解释器打印出错误堆栈，但程序也被结束了
可以把错误堆栈进行打印，然后分析错误原因，同时让程序继续执行下去"""

"""Py内置的logging模块可以记录错误信息"""
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as error:
        logging.exception(error)    # 打印错误信息

main()                              # 打印错误信息后程序继续执行
print('end'.upper())                # 执行
