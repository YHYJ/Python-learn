# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawl_project.items import HrTXListItem, HrTXDetailsItem


class HrTxSpider(CrawlSpider):
    name = 'hr_TX'
    allowed_domains = ['hr.tencent.com']

    # start_urls里的请求作用仅是经过所有的Rule来提取链接
    # 并不解析响应，因为没有回调函数
    start_urls = ['http://hr.tencent.com/position.php?&start=0']

    # LinkExtractor(allow=r"正则表达式")    :提取链接，返回响应
    # callback="回调函数"   :解析响应
    # follow=True/False     :是否继续跟踪
    """无论Rule的数量
    follow=True的响应都会经过所有的Rule进行处理
    follow=False的响应不会再经过任何Rule"""
    rules = (
        Rule(
            LinkExtractor(allow=r'start=\d+'),
            callback='parse_item',
            follow=True
        ),
        Rule(
            LinkExtractor(allow=r'position_detail\.php\?id=\d+'),
            callback='parse_details',
            follow=False
        ),
    )

    def parse_item(self, response):
        """解析招聘信息列表页"""
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = HrTXListItem()   # 代表一个职位信息
            item["post_name"] = node.xpath(".//a/text()").extract_first()
            item["post_link"] = node.xpath(".//a/@href").extract_first()
            item["post_type"] = node.xpath(".//td[2]/text()").extract_first()
            item["post_nums"] = node.xpath(".//td[3]/text()").extract_first()
            item["work_site"] = node.xpath(".//td[4]/text()").extract_first()
            item["issue_time"] = node.xpath(".//td[5]/text()").extract_first()

            yield item

    def parse_details(self, response):
        """解析招聘信息详情页"""
        item = HrTXDetailsItem()
        item["job_duties"] = " ".join(response.xpath(
            "//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        )
        item["job_demand"] = " ".join(response.xpath(
            "//ul[@class='squareli']")[1].xpath("./li/text()").extract()
        )

        yield item
