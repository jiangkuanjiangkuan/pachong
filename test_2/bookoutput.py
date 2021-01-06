#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class BookOutput(object):
    def __init__(self):
        self.datas = []

    def add_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def out_data(self):

        print(self.datas)