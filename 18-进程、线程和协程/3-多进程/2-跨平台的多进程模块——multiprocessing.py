#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""multiprocessing模块是Py中跨平台版本的多进程模块"""


"""如果写多进程的服务程序，Unix/Linux无疑是正确的选择
Windows没有fork调用，但由于Py是跨平台的，自然也应该提供一个跨平台的多进程支持
multiprocessing模块就是跨平台版本的多进程模块
"""

"""multiprocessing模块提供了一个Process类来代表一个进程对象"""
# 启动一个子进程并等待其结束：
import multiprocessing
import os

def run_process(name):
    print("运行子进程 %s (子线程ID：%s)..." % (name,os.getpid()))	# 获得子进程id，getppid是获得父进程id
    print("子线程test的父进程ID： %s ..." % (os.getppid()))
    print("子线程test的ID：%s..." % multiprocessing.current_process().pid)

if __name__ == '__main__':
    print("父进程的ID：%s." % os.getpid())
    p = multiprocessing.Process(target=run_process, args=('test',))
    print("子进程即将开始运行.")
    p.start()
    p.join()
    print("子进程结束.")
'''创建子进程时只需传入一个执行函数及其参数，创建一个Process实例，用start()方法启动
join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步'''
