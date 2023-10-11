#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Process之间需要通信，操作系统提供了很多机制来实现进程间的通信"""


"""Py的multiprocessing模块包装了底层的机制
提供了Queue(队列)、Pipes(管道)等多种方式来交换数据"""
# 在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import Process,Queue
import os, time, random


def write(q):
    """写数据的进程的代码"""
    print("写功能进程：%s" % os.getpid())
    for value in ['妖君','YJ','1516',]:
        print("将 %s 写入队列..." % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    """读数据的进程的代码"""
    print("读功能进程：%s" % os.getpid())
    while True:
        value = q.get(True)
        print("从队列读取 %s." % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
    pr.start()
    # 等待pw结束：
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()
'''
在类Unix下，multiprocessing模块封装了fork()调用，开发者不需要关注fork()的细节
由于Windows没有fork调用，multiprocessing需要“模拟”出fork的效果
父进程所有Py对象都必须通过pickle序列化再传到子进程去-
-所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
'''