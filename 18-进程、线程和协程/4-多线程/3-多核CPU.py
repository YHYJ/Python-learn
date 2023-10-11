#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import multiprocessing


def loop():
    """死循环"""
    x = 0
    while True:
        x = x ^ 1

'''死循环线程：
for i in range(multiprocessing.cpu_count()):    # 获取CPU核心数
    t = threading.Thread(target=loop)
    t.start()
'''
'''启动与CPU核心数量相同的N个线程：
用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满-
-4核就跑到400%，8核就跑到800%

用Py写的死循环在4核CPU上监控到CPU占用率仅有102%，也就是仅使用了一核-
-因为Py的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：
    Global Interpreter Lock
-任何Py线程执行前，必须先获得GIL锁，然后每执行100条字节码，解释器自动释放GIL锁-
-让别的线程有机会执行
这个GIL全局锁实际上把所有线程的执行代码都上了锁，所以多线程在Py中只能交替执行-
-即使100个线程跑在100核CPU上，也只能用到1个核

GIL是Py解释器设计的历史遗留问题，通常用的解释器是官方实现的CPy-
-要真正利用多核，除非重写一个不带GIL的解释器

所以，在Py中，可以使用多线程，但不能有效利用多核-
-如果一定要通过多线程利用多核，那只能通过C扩展来实现，但这就失去了Py简单易用的特点

Py虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务-
-多个Py进程有各自独立的GIL锁，互不影响
'''