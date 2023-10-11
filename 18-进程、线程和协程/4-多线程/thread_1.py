#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-13 20:39:26
Last modified: 2017-09-13 20:39:26
Python release: 3.6.2

线程执行顺序
"""


import threading, time

def sing():
    for i in range(3):
        print("子线程 %s >>> %s" % (threading.current_thread().name, i))
        print("%d 正在唱歌..." % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("子线程 %s >>> %s" % (threading.current_thread().name, i))
        print("%d 正在跳舞..." % i)
        time.sleep(8)


if __name__ == '__main__':
    print("主线程 %s 开始" % threading.current_thread().name)
    t1 = threading.Thread(target=sing, name='SingThread')
    t2 = threading.Thread(target=dance, name='DanceThread')

    # 将t1、t2子线程设置为守护线程，因此主进程不会阻塞
    t1.daemon = True
    t2.daemon = True

    t1.start()
    t2.start()

    # 阻塞主进程，因此只有join执行完成后才会继续执行主进程
    t1.join()
    t2.join()

    print("主进程 %s 结束" % threading.current_thread().name)

    """种情况
    1. 只设置了daemon而没设置join:
        主线程没有被阻塞，当主线程完成后，子线程也随之被关闭
    2. 只设置了join而没设置daemon：
        主线程被join阻塞，只有所有子线程都完成后，主线程才会关闭
        当某个子线程里有循环时，强制停止程序只会停止没有循环的子线程，因此主线程不会退出，
        还需要单独停止有循环的线程整个程序才会停止
    3. join和daemon都没有设置：
        没有线程被阻塞，所有线程都得到执行，主线程关闭并不会影响子线程
    4. join和daemon都设置了：
        在没有循环的情况下和2一样，当某个子线程（或全部子线程）里有循环，
        强制停止程序会导致主线程得以执行，因此整个程序都随之关闭
    """
