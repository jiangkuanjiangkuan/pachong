#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class BookManger(object):
    def __init__(self):
        self.new_bookurls = set()
        self.old_bookurls = set()

    def get_newurl(self):
        new_url = self.new_bookurls.pop()
        return new_url
    def add_newurl(self,url):
        if url is None:
            return
        self.new_bookurls.add(url)