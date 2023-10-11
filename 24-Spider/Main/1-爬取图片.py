#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: YJ1516 - YJ1516268@outlook.com
Date: 2017-09-24 20:17:24
Last modified: 2017-09-24 20:17:24
Python release: 3.6.2

爬取图片
<https://image.baidu.com/>
"""


import gevent
import urllib.request
from gevent import monkey, pool

monkey.patch_all()

# jobs = []
# p = pool.pool(6)


def download(file_name, url):
    print("GET： %s" % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as fi:
        fi.write(data)

    print("%d bytes recv from %s." % (len(data), url))

urls = [
        'https://rpic.douyucdn.cn/appCovers/2017/09/13/688928_20170913203807_big.jpg',
        'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506862503&di=9a6e3ae0fd45f99e464f570508f5e243&imgtype=jpg&er=1&src=http%3A%2F%2Fimgsrc.baidu.com%2Fimage%2Fc0%253Dshijue1%252C0%252C0%252C294%252C40%2Fsign%3Dde34d31022381f308a1485eac168267d%2Fe824b899a9014c082e1dc98d007b02087bf4f4f0.jpg'
]

'''
for url in urls:
    jobs.append(p.spawn(download, url))
gevent.joinall(jobs)
'''
gevent.joinall([
    gevent.spawn(download, "1.jpg", urls[0]),
    gevent.spawn(download, "2.jpg", urls[1]),
])

