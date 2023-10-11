#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ
Email: yj1516268@outlook.com
Created Date: 2018-09-03 10:51:03

"""

import asyncio
import threading


@asyncio.coroutine
def hello():
    print("Hello world! ({})".format(threading.currentThread()))
    yield from asyncio.sleep(3)     # 模拟IO操作
    print("Hello again! ({})".format(threading.currentThread()))


loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
