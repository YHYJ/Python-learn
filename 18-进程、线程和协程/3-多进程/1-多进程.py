#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""多进程(multiprocessing)"""


"""Unix/Linux操作系统提供了一个很特殊的 fork() 系统调用：
普通的函数调用，调用一次，返回一次，但fork()调用一次，返回两次
因为操作系统自动把当前进程（父进程）复制一份（子进程）
然后分别在父进程和子进程内返回fork()的调用
"""

"""fork()系统调用的返回：
子进程永远返回0，而父进程返回子进程的ID
这样做的理由是：一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID-
            -而子进程只需要调用getppid()就可以拿到父进程的ID
"""


"""Python的os模块封装了常见的系统调用，其中就包括fork"""
# 可以在Py程序中轻松创建子进程：
import os

print("进程(%s)启动..." % os.getpid())     # 只运行在类Unix系统
pid = os.fork()     # 创建子进程
if pid == 0:
    print("(%s)是个子进程，它的父进程是(%s)." % (os.getpid(),os.getppid()))
else:
    print("(%s)刚创建了一个子进程(%s)." % (os.getpid(),pid))

'''由于Windows没有fork调用，上面的代码在Windows上无法运行'''

"""有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
常见的Apache服务器就是由父进程监听端口
每当有新的http请求时，就fork出子进程来处理新的http请求"""














