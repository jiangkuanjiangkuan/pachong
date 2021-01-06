# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def open(self):
        pass
    #     打开文件

    def colose(self):
    #     关闭
        pass
    def process_item(self, item, spider):
        # 数据的处理，检验，存到数据库

        return item
