#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
fib(15)

'''结果没问题，但是.

再接再fib函数中用print打印数字会导致该函数可复用性差，
因为fib函数返回None，其它函数无法获得该函数生成的数列.'''
