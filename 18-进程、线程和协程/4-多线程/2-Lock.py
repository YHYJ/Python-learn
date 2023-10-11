#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""多线程和多进程最大的不同在于：
多进程中，同一个变量各自有一份拷贝存在于每个进程中，互不影响
多线程中，所有变量由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了"""


# 多个线程同时操作一个变量把内容改乱的例子：
import time
import threading

money = 0       # 银行存款


def change_it(n):
    """先存后取，结果应该为0"""
    global money    # 声明money为全局变量
    money += n
    money -= n


def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
# t1.join()  # 相当于的单线程
t2.start()
t1.join()
t2.join()
print(money)
'''定义了一个共享变量money = 0
启动两个线程，先存后取，理论上结果应该为0
但由于线程的调度是由操作系统决定的
当t1、t2交替执行时，只要循环次数足够多，money的结果就不一定是0了
因为修改money需要多条语句，而执行这几条语句时，线程可能中断-
-从而导致多个线程把同一个对象的内容改乱了
'''


"""
两个线程同时一存一取，就可能导致余额不对-
-必须确保一个线程在修改money的时候，别的线程一定不能改
如果要确保money计算正确，就要给change_it()上一把锁-
-当某个线程开始执行change_it()时，该线程因为获得了锁-
-因此其他线程不能同时执行change_it()，只能等待-
-直到锁被释放后，获得该锁以后才能改
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁-
-所以不会造成修改的冲突
"""
# 创建一个锁通过threading.Lock()来实现：
money_1 = 0
lock = threading.Lock()


def change_it_1(n):
    """先存后取，结果应该为0"""
    global money_1    # 声明money_1为全局变量
    money_1 += n
    money_1 -= n


def run_thread_1(n):
    for i in range(1000000):
        lock.acquire()     # 核心代码上锁
        try:
            change_it_1(n)  # 改数据
        finally:
            lock.release()  # 释放锁

t3 = threading.Thread(target=run_thread_1,args=(5,))
t4 = threading.Thread(target=run_thread_1,args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()
print(money_1)
'''当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁-
-然后继续执行代码，其他线程就继续等待直到获得锁为止

获得锁的线程用完后一定要释放锁，否则其他线程将永远等待下去，成为死线程-
-所以用try...finally来确保锁一定会被释放

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多：
    首先是阻止了多线程并发执行-
        -包含锁的某段代码实际上只能以单线程模式执行，效率大幅下降
    其次，由于可以存在多个锁-
        -不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁-
        -导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止
'''
