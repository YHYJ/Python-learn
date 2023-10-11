#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-24 15:19:37
Last modified: 2017-09-24 15:19:37
Python release: 3.6.2

通过yield实现协程
"""


import time

def work1():
    while True:
        print("---work1---")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("---work2---")
        yield
        time.sleep(1.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == "__main__":
    main()

