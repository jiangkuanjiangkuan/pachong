#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
class BookPader(object):
    def parser(self,bookurl,bookcontent):
        if bookurl is None:
            return
        soup = BeautifulSoup(bookcontent,'html.parser')
        bookdata  = self._getbookdata(bookurl,soup)
        return bookdata

    def _getbookdata(self,bookurl,soup):
        bookdata = {}
        # bookdata['连接'] = bookurl
        # print(len(soup.find_all('div', class_="info")))
        for i in soup.find_all('div', class_="info"):
            # 爬取parser========
            bookdata['书名'] = i.find("h2").get_text()
            bookdata[2] = i.find('div', class_='pub').get_text()
            bookdata[3] = float(i.find('span', class_='rating_nums').get_text())
            bookdata[4] = i.find('span', class_='pl').get_text()

            # text  = i.find("p").get_text()
            # print(i)
            return bookdata
