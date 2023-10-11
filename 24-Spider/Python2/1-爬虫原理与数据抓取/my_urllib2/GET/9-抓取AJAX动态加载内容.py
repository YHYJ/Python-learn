#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""对于使用ajax动态加载的内容，无法直接对网页URL进行获取
ajax请求一般返回的是JSON文件，只要对ajax请求地址进行POST或GET就能获得JSON数据

所以抓取ajax动态内容的关键就是抓包找出ajax请求地址
"""

import urllib

from plugs_one.spider import spider


def movie_douban_spider():
    """
    豆瓣电影
    :return:
    """
    start = int(raw_input("从第几名开始："))
    limit = int(raw_input("到第几名结束："))

    url = "https://movie.douban.com/j/chart/top_list?"

    arguments = {
        'type': '11',
        'interval_id': '100:90',
        'action': ''
    }
    real_argus = urllib.urlencode(arguments)

    long_url = url + real_argus  # 拼接URL

    for page in range(start, limit + 1):
        num = page - 1

        full_url = long_url + "&start=" + str(num) + "&limit=" + str(1)

        # 存储结果
        file_name = "豆瓣电影TOP{}_NO{}.json".format(limit, page)

        spider(full_url, file_name, timeout=3)


if __name__ == '__main__':
    movie_douban_spider()
