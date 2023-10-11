#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""要启动大量的子进程可以使用进程池，通过Pool类"""

import multiprocessing
import time
import random
import os


"""如果要启动大量的子进程"""
# 可以用进程池的方式批量创建子进程：


def long_time_task(name):
    print("运行任务 %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("任务 %s 运行了 %.2f 秒." % (name, (end-start)))
    # open('a' + str(name), 'w').write(str(name))


if __name__ == '__main__':
    print("父进程 %s." % os.getpid())
    p = multiprocessing.Pool(5)
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))    # 创建任务
    print("等待所有子进程完成...")
    p.close()
    time.sleep(1)
    p.join()
    print("所有子进程已完成.")
'''代码解读：
对Pool对象调用join()方法会等待所有子进程执行完毕
调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了

注意输出的结果，任务0,1,2,3是立刻执行的，而任务4要等待前面某个任务完成后才执行
这是因为Pool的默认大小在此电脑上是4，因此最多同时执行4个进程
这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
p = Pool(5)
就可以同时跑5个进程

由于Pool的默认大小是CPU的核数，如果是8核CPU，
要提交至少9个子进程才能看到上面的等待效果
'''
