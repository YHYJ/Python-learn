#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
from collections import deque


queue = deque()
visited_url = set()  # 已抓取URL

url = "https://jecvay.com/"    # 入口URL

queue.append(url)
cnt = 0  # 已爬取URL数量

while queue:
    url = queue.popleft()   # 取得队列中第一个元素并删除
    '''抓取该URL之前将其加入visited_url'''
    visited_url.add(url)

    print("已抓取：{} <-|-> 正在抓取---> {}".format(cnt, url))
    cnt += 1

    try:
        url_open = urllib.request.urlopen(url, timeout=3)
        '''getheader()函数获取抓取到的文件类型'''
        if "html" not in url_open.getheader("Content-Type"):
            continue
        data = url_open.read().decode("UTF-8")
    except Exception as e:
        print(e)
        continue

    '''正则提取data中符合的元素，并判断是否已抓取，否则加入queue队列'''
    link = re.compile("href='(.+?)'")  # 预编译正则表达式
    for x in link.findall(data):
        if "http" in x and x not in visited_url:
            queue.append(x)
            print("{} --->加入队列".format(x))
