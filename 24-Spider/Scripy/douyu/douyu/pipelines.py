# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
import pymongo

from scrapy.pipelines.images import ImagesPipeline

from douyu.settings import IMAGES_STORE


class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        """发送图片请求"""
        yield scrapy.Request(item["avatar_mid"])

    def item_completed(self, results, item, info):
        """处理图片信息"""
        image_path = [x["path"] for ok, x in results if ok][0]

        # 文件名
        new_name = IMAGES_STORE + item['nickname'] + ".jpg"
        item["image_path"] = new_name

        old_name = IMAGES_STORE + image_path

        try:
            os.rename(old_name,  item['image_path'])
        except Exception:
            pass

        return item
    range()


class SaveToMongoPipeline(object):
    """将信息存入MongoDB"""
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        self.db = self.client["DouyuDirector"]
        self.collection = self.db["item"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
