#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""多任务可以由多进程完成，也可以由一个进程内的多线程完成
进程是由若干线程组成的，一个进程至少有一个线程"""


import time
import threading

"""线程是操作系统直接支持的执行单元，因此Py内置多线程的支持
并且Py的线程是真正的Posix Thread(Posix线程)，而不是模拟出来的线程"""

"""Py标准库提供了两个模块：_thread和threading，_thread是低级模块
threading是高级模块，对_thread进行了封装
绝大多数情况下只需要使用threading这个高级模块"""


"""启动一个线程就是创建一个Thread实例并传入一个函数"""
# 然后调用start()开始执行：


def loop():
    """执行一个新线程的代码"""
    print("子线程 %s 正在运行..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("子线程 %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(0.5)
    print("子线程 %s 结束." % threading.current_thread().name)

print("主线程 %s 正在运行..." % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
#根据输出可知有两个线程：主线程MainThread和子线程LoopThread
t.start()
t.join()        # 阻塞直至当前调用join的线程结束。在此，不加join的话会在主线程结束的时候就执行下面的print
print("主线程 %s 结束." % threading.current_thread().name)

'''任何进程默认就会启动一个线程，该线程称为主线程，主线程又可以启动新的线程
Py的threading模块有个current_thread()函数，它永远返回当前线程的实例
主线程实例的名字叫MainThread，子线程的名字在创建时指定为LoopThread
名字仅用来显示，完全没有其他意义，如果不起名字Py会自动给线程命名为Thread-1，Thread-2……
'''
