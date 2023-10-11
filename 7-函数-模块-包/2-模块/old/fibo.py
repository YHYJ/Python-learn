#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):    #输出直到 n 的斐波那契数列
    a,b = 0,1
    while b < n:
        print(b,end = ' ')
        a,b = b,a + b
        print()

def fib2(n):    #以数列形式返回到 n 的斐波那契数列
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)
        a,b = b,a + b
    print(result)

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))