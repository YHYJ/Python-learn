#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""10线程访问10次网页用时"""

import threadpool
import requests
import time

start_time = time.time()


def run(url):
    r = requests.get(url)


pool = threadpool.ThreadPool(10)

reqs = threadpool.makeRequests(run, args_list=['https://www.liaoxuefeng.com/'
                                               for x in range(10)])
[pool.putRequest(x) for x in reqs]
pool.wait()
print("用时：{}秒".format(time.time() - start_time))
# 30s
