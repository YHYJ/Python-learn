# -*- coding: utf-8 -*-

import scrapy

from hr_TX.items import HrTxItem, PostItem


class HrTxXpathSpider(scrapy.Spider):
    name = 'hr_TX_xpath'
    allowed_domains = ['hr.tencent.com']
    basic_url = 'http://hr.tencent.com/position.php?&start='

    start_urls = ["{}{}".format(basic_url, num)for num in range(0, 101, 10)]
    # start_urls = [basic_url + str(num) for num in range(0, 101, 10)]
    # start_urls = ["http://hr.tencent.com/position.php?&start=" +
    #               str(num) for num in range(0, 101, 10)]

    def parse(self, response):
        """处理招聘信息列表页
        :yield: url: 深入URL
        :yield: meta: 回调函数的参数
        :yield: callback: 回调函数，调用self.parse_page
        """
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = HrTxItem()

            item["post_name"] = node.xpath(".//a/text()").extract_first()
            item["post_link"] = "http://hr.tencent.com/{}".format(
                node.xpath(".//a/@href").extract_first()
            )
            item["post_type"] = node.xpath("./td[2]/text()").extract_first()
            item["post_nums"] = node.xpath("./td[3]/text()").extract_first()
            item["post_site"] = node.xpath("./td[4]/text()").extract_first()
            item["post_time"] = node.xpath("./td[5]/text()").extract_first()

            yield item
            yield scrapy.Request(url=item["post_link"],
                                 callback=self.parse_page)

    def parse_page(self, response):
        """处理招聘信息详情页"""
        item = PostItem()

        item["job_duties"] = " ".join(response.xpath(
            "//ul[@class='squareli']")[0].xpath("./li/text()").extract())
        item["job_demand"] = " ".join(response.xpath(
            "//ul[@class='squareli']")[1].xpath("./li/text()").extract())

        yield item
