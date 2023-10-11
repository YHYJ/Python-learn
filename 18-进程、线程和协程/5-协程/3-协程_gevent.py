#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-24 16:12:57
Last modified: 2017-09-24 16:12:57
Python release: 3.6.2

自动切换协程子程序的模块——gevent
"""


"""gevent是基于协程的Py网络库，通过greenlet实现协程
其基本思想是：当一个greenlet遇到IO操作比如访问网络时就自动切换到其他greenlet，
等到IO操作完成，再在适当的时候切换回来继续运行
"""

import urllib.request
import gevent
from gevent import monkey

'''
def f(num):
    for i in range(num):
        print(gevent.getcurrent(), i)
        gevent.sleep(int(num)/10)   # 交出控制权，使greenlet交替运行
        # 也可以使用time.sleep()，但需要在函数外声明 monkey.patch_all()


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()'''
'''不加line 25的延时来模拟耗时操作的话，3个greenlet是依次运行而非交替运行
可以使用gevent.sleep()模拟耗时操作
'''


"""实际代码里不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换
由于切换是在IO操作时自动完成，所以gevent需要修改Py自带的一些标准库
这一过程在启动时通过monkey.patch_all()完成"""
monkey.patch_all()  # 在有IO操作时用，实现协程的并发


def func(url):
    print("GET：%s" % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print("%d bytes recv from %s." % (len(data), url))

gevent.joinall([
    gevent.spawn(func, "https://www.zhihu.com/"),
    gevent.spawn(func, "https://www.weibo.com/"),
    gevent.spawn(func, "https://www.bilibili.com/"),
])
'''结果显示3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程'''

