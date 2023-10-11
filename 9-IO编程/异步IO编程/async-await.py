#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ
Email: yj1516268@outlook.com
Created Date: 2018-09-03 11:20:44

"""

import asyncio
import threading


async def hello():
    try:
        print("Hello world! {}".format(threading.currentThread()))
        data = await asyncio.sleep(1)
        print("Hello again! {}".format(threading.currentThread()))
    except Exception as e:
        # print(e)
        pass
    return data


tasks = [hello(), hello(), hello()]
loop = asyncio.get_event_loop()                 # 获取event loop
loop.run_until_complete(asyncio.wait(tasks))    # 执行协程
loop.close()


print("++++++++++++++++++++++++++")
print("{} tasks = {}".format(type(tasks), tasks))
print("{} loop = {}".format(type(loop), loop))
