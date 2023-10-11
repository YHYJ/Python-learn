#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""urllib 和 urllib2 都是接受URL请求的相关模块，但是提供了不同的功能
最显著的不同如下：
    1.urllib 模块仅可以接受URL，不能创建设置了 headers 的 Request 类实例
    2.但是 urllib 提供 urlencode 方法用来产生GET查询字符串，而 urllib2 则没有，
      这是 urllib 和 urllib2 经常一起使用的主要原因
编码工作使用 urllib 的 urlencode() 函数，将key:value这样的键值对，转换成"key=value"这样的字符串
解码工作可以使用 urllib 的 unquote() 函数
"""

import random
import urllib   # 负责URL编码处理
import urllib2

from Python2.conf.User_Agent_list import USER_AGENT_LIST


def search(wd):
    """百度搜索 “火狐” """
    url = "http://www.baidu.com/s"
    word = {"wd": wd}
    word = urllib.urlencode(word)  # 转换成URL编码格式（字符串）
    full_url = url + "?" + word

    user_agent = random.choice(USER_AGENT_LIST)

    request = urllib2.Request(full_url)

    request.add_header("User-Agent", user_agent)

    response = urllib2.urlopen(request)

    html = response.read()

    wd = urllib.unquote(wd)
    file_name = "/home/yj/Documents/Project/Python/Python-minute/" \
                "24-爬虫/Python2/1-爬虫原理与数据抓取/GET/data/html/" \
                "6_百度搜索“{}”.html".format(wd)
    with open(file_name, mode="w") as f:
        f.write(html)


if __name__ == '__main__':
    wd = raw_input("输入关键字：")
    search(wd)
