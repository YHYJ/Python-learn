#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib

from plugs_one.spider import spider


def bdtb_spider():
    """
    抓取指定百度贴吧指定页面
    第一页：http://tieba.baidu.com/f?kw=lol&pn=0
    第二页： http://tieba.baidu.com/f?kw=lol&pn=50
    第三页： http://tieba.baidu.com/f?kw=lol&pn=100
    :param url:
    :param a_page:
    :param z_page:
    :return:
    """
    kw = raw_input("输入贴吧名：")
    a_page = int(raw_input("输入起始页："))
    z_page = int(raw_input("输入结束页："))

    url = "http://tieba.baidu.com/f?"   # URl主体
    keyword = urllib.urlencode({"kw": kw})  # 请求关键字
    url = url + keyword  # URL + 关键词

    for page in range(a_page, z_page + 1):

        num = (page - 1) * 50

        full_url = url + "&pn=" + str(num)

        file_name = "{}吧第{}页.html".format(kw, page)

        spider(full_url, file_name, timeout=6)


if __name__ == '__main__':
    bdtb_spider()
