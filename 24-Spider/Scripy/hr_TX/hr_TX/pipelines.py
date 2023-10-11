# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime

from hr_TX.items import HrTxItem, PostItem


class HrTxPipeline(object):
    """处理HrTxItem"""
    def __init__(self, spider):
        """当爬虫开启时调用"""
        self.file_name = open("./data/hr_TX_list.csv", "w")

    def process_item(self, item, spider):
        """处理item"""
        if isinstance(item, HrTxItem):
            item["data_from"] = spider.name
            item["data_time"] = str(datetime.utcnow())

            content = "{},\n".format(item)
            self.file_name.write(content)
        return item

    def close_spider(self, spider):
        """当爬虫关闭时调用"""
        self.file_name.close()


class PostPipeline(object):
    """处理PostItem"""
    def __init__(self, spider):
        self.file_name = open("./data/hr_TX_details.csv", "w")

    def process_item(self, item, spider):
        if isinstance(item, PostItem):
            item["data_from"] = spider.name
            item["data_time"] = str(datetime.utcnow())

            content = "{},\n".format(item)
            self.file_name.write(content)
        return item

    def close_spider(self, spider):
        self.file_name.close()
