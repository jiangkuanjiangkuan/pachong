#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
class BookDownloader(object):
    def book_downloader(self,url):
        if url is None:
            return None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }  # 浏览器头描述
        data = requests.get(url, headers=headers)
        # print(data.text)
        data.encoding = 'utf-8'
        # print(data.content)
        return data.content
