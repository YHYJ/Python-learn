# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from datetime import datetime

from crawl_project.items import HrTXListItem, HrTXDetailsItem


class HrTXListPipeline(object):
    def __init__(self, spider):
        self.file_name = open("hr_TX_list.csv", "w")

    def process_item(self, item, spider):
        if isinstance(item, HrTXListItem):
            item["data_source"] = spider.name    # 爬虫名作为数据源
            item["crawl_time"] = str(datetime.utcnow())

            content = "{},\n".format(item)
            self.file_name.write(content)

        return item

    def close_spider(self, spider):
        self.file_name.close()


"""每个item对象都会经过所有管道"""


class HrTXDetailPipeline(object):
    def __init__(self, spider):
        self.file_name = open("hr_TX_details.csv", "w")

    def process_item(self, item, spider):
        if isinstance(item, HrTXDetailsItem):
            item["data_source"] = spider.name    # 爬虫名作为数据源
            item["crawl_time"] = str(datetime.utcnow())

            content = "{},\n".format(item)
            self.file_name.write(content)

        return item

    def close_spider(self, spider):
        self.file_name.close()
