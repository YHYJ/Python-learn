# -*- coding: utf-8 -*-

import scrapy

from bs4 import BeautifulSoup

from hr_TX.items import HrTxItem


class HrTxSpiderSpider(scrapy.Spider):
    name = 'hr_TX_spider'
    allowed_domains = ['hr.tencent.com']
    basic_url = 'http://hr.tencent.com/position.php?&start='

    start_urls = ["{}{}".format(basic_url, num) for num in range(0, 101, 10)]

    def parse(self, response):
        bs = BeautifulSoup(response, "lxml")

        node_list = bs.find_all("tr", {"class": ["even", "odd"]})

        for node in node_list:
            """创建item对象来存储，每个item都表示一个招聘信息"""
            item = HrTxItem()

            item["post_name"] = node.find("a").get_text()
            item["post_link"] = "{}{}".format(
                "http://hr.tencent.com/",
                node.find("a").get("href")
            )
            item["post_type"] = node.find("td")[1].get_text()
            item["post_nums"] = node.find("td")[2].get_text()
            item["post_site"] = node.find("td")[3].get_text()
            item["post_time"] = node.find("td")[4].get_text()
            item["data_from"] = node.find("td")[5].get_text()
            item["data_time"] = node.find("td")[6].get_text()

            yield item
