#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

class BookSpider(scrapy.Spider):
    name = 'douban_book'

    start = ['https://book.douban.com/top250']


    def parse(self, response):
        yield scrapy.Request(response.url,callback=self.bookparser)

    def bookparser(self):

        pass
