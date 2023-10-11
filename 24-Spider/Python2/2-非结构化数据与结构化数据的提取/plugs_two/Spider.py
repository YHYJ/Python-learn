#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import requests
from lxml import etree

from conf.User_Agent_list import USER_AGENT_LIST


class Spider:
    """爬虫类"""
    def __init__(self, de_code="utf-8", en_code="utf-8"):
        """
        :param de_code: 网页原始编码
        :param en_code: 转换编码
        """
        self.de_code = de_code
        self.en_code = en_code
        self.user_agent = random.choice(USER_AGENT_LIST)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        """
        爬虫主体
        :return:
        """
        print("正在抓取：{}".format(url))
        response = requests.get(url, headers=self.headers)

        return response.content # .decode(self.de_code).encode(self.en_code)

    def spider_link(self, response, xpath_rule):
        """
        获取响应里的链接
        :param response: 获取 send_request() 方法抓取的网页源码
        :param xpath_rule: 获取标签的 xpath 规则
        :return:
        """
        html = etree.HTML(response)
        link_list = html.xpath(xpath_rule)

        return link_list

    def spider_image(self, response, xpath_rule):
        """
        获取响应里的图片链接
        :param response: 获取 send_request() 方法抓取的网页源码
        :param xpath_rule: 获取标签的 xpath 规则
        :return:
        """
        html = etree.HTML(response)
        link_list = html.xpath(xpath_rule)

        return link_list
