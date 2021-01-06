# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 数据收集
    name = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    publisher = scrapy.Field()
    ratings = scrapy.Field()
