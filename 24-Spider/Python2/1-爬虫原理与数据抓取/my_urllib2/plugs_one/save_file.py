#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def save_file(html, file_name):
    """
    存储抓取的结果
    :param html:
    :param file_name:
    :return:
    """
    full_name = "/home/yj/Documents/Project/Python/Python-minute/" \
                "24-爬虫/Python2/1-爬虫原理与数据抓取/my_urllib2/data/html/" \
                + file_name

    print "正在写入：<{}>".format(file_name)
    print "文件路径：<{}>\n".format(full_name)

    with open(full_name, "w") as f:
        f.write(html)

    print "-" * 32
