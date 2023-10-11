# -*- coding: utf-8 -*-

import json
import scrapy

from douyu.items import DouyuItem


class DouyusSpider(scrapy.Spider):
    name = 'douyus'
    allowed_domains = ['douyucdn.cn']

    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        datas = json.loads(response.body)["data"]

        if datas:
            for data in datas:
                item = DouyuItem()
                item["room_id"] = data["room_id"]
                item["room_name"] = data["room_name"]
                item["nickname"] = data["nickname"]
                item["game_name"] = data["game_name"]
                item["anchor_city"] = data["anchor_city"]
                item["avatar_mid"] = data["avatar_mid"]
                yield item

            self.offset += 20
            yield scrapy.Request(url = self.url + str(self.offset), callback=self.parse)
