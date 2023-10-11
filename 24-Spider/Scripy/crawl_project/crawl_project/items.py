# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HrTXListItem(scrapy.Item):
    """职位名、详情链接、职位类别、招聘人数、工作地点、发布时间、数据源、抓取时间"""
    post_name = scrapy.Field()
    post_link = scrapy.Field()
    post_type = scrapy.Field()
    post_nums = scrapy.Field()
    work_site = scrapy.Field()
    issue_time = scrapy.Field()
    data_source = scrapy.Field()
    crawl_time_ = scrapy.Field()


class HrTXDetailsItem(scrapy.Item):
    """工作职责、工作要求、数据源、抓取时间"""
    job_duties = scrapy.Field()
    job_demand = scrapy.Field()
    data_source = scrapy.Field()
    crawl_time = scrapy.Field()
