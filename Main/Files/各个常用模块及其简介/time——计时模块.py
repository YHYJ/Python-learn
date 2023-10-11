#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""time 模块提供与时间相关的方法"""
'''利用time，可以简单的计算出程序运行的时间。对于一些比较复杂、耗时较多的程序，可以了解程序中哪里是效率瓶颈来进行优化'''
'''在计算机领域有一个特殊时间叫做 epoch ，它表示的时间是1970-01-01 00:00:00 UTC'''
#1：python中time模块的一个方法返回的就是从epoch到当前的秒数（不考虑闰秒），这个值被称为unix时间戳
import time
print(time.time())

#1：于是可以用这个方法得到程序的运行时间：
startime = time.time()
print('start:%f'%startime)
for i in range(1000000):
    pass
endtime = time.time()   #在程序的不同位置调用time.time()就可以得到运行到那个地方的时间，了解不同部分消耗的时间
print('end:%f'%endtime)
print('程序运行时间:%fs'%(endtime-startime))
#有了这个方法，我们还可以在Pygame课程中的打飞机游戏里，得到每一次游戏主循环刷新的时间，计算出游戏的每秒帧数，显示在屏幕上


#2：使程序暂停secs秒：time.sleep(secs)
start = time.time()
print('开始')
time.sleep(3)
print('结束')
end = time.time()
print('运行时间：%f'%(end-start))
#在抓取网页的时候，适当让程序sleep一下，可以减少短时间内的请求，提高请求的成功率
