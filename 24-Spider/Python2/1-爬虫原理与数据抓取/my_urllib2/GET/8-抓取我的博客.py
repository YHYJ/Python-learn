#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plugs_one.spider import spider


def bdtb_spider():
    """
    抓取我的博客
    :param max_num: 抓取的文章篇数
    :return:
    """
    max_num = int(raw_input("输入抓取文章篇数："))

    url = "http://yj1516.site/post/"

    for num in range(1, max_num + 1):
        full_url = url + str(num)

        file_name = "我的博客第{}篇.html".format(num)

        spider(full_url, file_name, timeout=2)


if __name__ == '__main__':
    bdtb_spider()
