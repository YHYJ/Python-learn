#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-23 20:28:36
Last modified: 2017-09-23 20:28:36
Python release: 3.6.2

Py对协程的支持是通过generator(生成器)实现的
"""


"""生成器，不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值
但Py的yield不但可以返回一个值，还可以接收调用者发出的参数"""


# 例子：
"""传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待
但一不小心可能死锁
改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行
等消费者执行完毕后，切换回生产者继续生产"""
def consumer():
    """消费者，是一个生成器"""
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[消费者] <%s> 消费中..." % n)
        r = '200 OK'


def produce(c):
    """生产者"""
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[生产者] <%s> 生产中..." % n)
        r = c.send(n)
        print("[生产者]消费者返回：%s" % r)
    c.close()

c = consumer()
produce(c)
'''
c = consumer()获得一个生成器对象c，把c传入produce()
1、首先执行line 36启动生成器
2、接着执行line 37/38/39/40，生产一个消息，line 41将n = 1传入到consumer并执行这个函数
3、c.send(n)唤醒yield，处理消息，打印line 30，通过yield返回r = '200 OK'
4、produce函数了、line 41接收r的值，打印结果
5、循环，当n = 5时，执行line 43关闭生成器对象，不再生产消息，过程结束
'''
'''整个过程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为‘协程’'''


"""协程的特点：
”子程序就是协程的一种特例“  —— Donald Knuth
"""
