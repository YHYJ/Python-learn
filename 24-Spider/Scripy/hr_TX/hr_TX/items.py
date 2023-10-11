# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HrTxItem(scrapy.Item):
    """职位列表页数据
    职位名、详细链接、职位类别、招聘人数、工作地点、发布时间、数据来源、抓取时间
    """
    post_name = scrapy.Field()
    post_link = scrapy.Field()
    post_type = scrapy.Field()
    post_nums = scrapy.Field()
    post_site = scrapy.Field()
    post_time = scrapy.Field()
    data_from = scrapy.Field()
    data_time = scrapy.Field()


class PostItem(scrapy.Item):
    """职位详情页数据
    工作职责、工作要求、数据来源、抓取时间
    """
    job_duties = scrapy.Field()
    job_demand = scrapy.Field()
    data_from = scrapy.Field()
    data_time = scrapy.Field()
