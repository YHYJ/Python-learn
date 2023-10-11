# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    """直播间ID、直播间名、昵称、分类、所在地、直播间截图、头像"""
    room_id = scrapy.Field()
    room_name = scrapy.Field()
    nickname = scrapy.Field()
    game_name = scrapy.Field()
    anchor_city = scrapy.Field()
    avatar_mid = scrapy.Field()
    image_path = scrapy.Field()
