#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""用XPath做一个爬虫，尝试爬取某个贴吧里的所有帖子
将帖子里每个楼层发布的图片下载到本地"""

import urllib

from plugs_two import tieba_info
from plugs_two.Spider import Spider
from plugs_two.Save import SaveData


def tap_spider(tb_name):
    """
    爬取某个贴吧里的所有帖子并且将该这个帖子里每个楼层发布的图片下载到本地
    :param tb_name: 贴吧名，关键字kw
    :return:
    """
    param = tieba_info()
    a_page = param["a_page"]
    e_page = param["e_page"]
    file_dir = param["file_dir"]

    '''标签提取规则'''
    link_xpath_rule = "//div[@class='t_con cleafix']/div/div/div/a/@href"
    image_xpath_rule = "//img[@class='BDE_Image']/@src"

    url = "http://tieba.baidu.com"

    for page in range(a_page, e_page + 1):
        pn = (page - 1) * 50    # 页码值
        url_param = {"pn": pn, "kw": tb_name}
        full_url_param = urllib.urlencode(url_param)    # 组合URL参数
        '''帖子列表页完整URL'''
        full_url = "{}{}{}".format(url, "/f?", full_url_param)

        spider = Spider()   # 爬虫类对象

        '''请求帖子列表页'''
        response = spider.send_request(full_url)
        '''传参帖子列表页响应和其提取规则，提取帖子列表里的帖子的链接'''
        link_list = spider.spider_link(response, link_xpath_rule)

        '''请求每个帖子链接'''
        for post_link in link_list:
            post_url = "{}{}".format(url, post_link)
            '''发送图片请求获取响应'''
            response = spider.send_request(post_url)
            '''提取图片链接'''
            image_link_list = spider.spider_image(response, image_xpath_rule)

            '''处理每张图片链接'''
            for image_link in image_link_list:
                image_data = spider.send_request(image_link)

                '''保存图片'''
                filename = image_link[-15:]
                save = SaveData(filename, file_dir)
                save.save_image(image_data)


if __name__ == '__main__':
    tb_name = raw_input("贴吧名：")
    tap_spider(tb_name)
