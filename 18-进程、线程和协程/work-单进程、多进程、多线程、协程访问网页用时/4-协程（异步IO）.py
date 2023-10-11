#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""协程访问10次网页用时"""

import asyncio, aiohttp, time

start_time=time.time()

async def run(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            pass

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(run('https://www.liaoxuefeng.com/'))
         for x in range(10)]
loop.run_until_complete(asyncio.wait(tasks))
print("用时：{}秒".format(time.time() - start_time))
# 0.8s
