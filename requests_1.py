#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# import requests
# from io import BytesIO
# from PIL import Image

# print(dir(requests))
# r = requests.get('http://www.baidu.com')
# print(r.text)
# print(r.status_code)
# print(r.encoding)

# j = {'jk1':'jkuan1','jk2':'jkuan2','jk3':None}
# k = requests.get('http://httpbin.org/get', j)
# print(k.url)
# print(k.text)

# ?????????????????????????????????????????????
# r = requests.get('http://img5.imgtn.bdimg.com/it/u=4214941395,707510718&fm=26&gp=0.jpg')
# image = Image.open(BytesIO(r.content))
# image.save('image_1.jpg')

# r = requests.get('https://github.com/timeline.json')
# print(type(r.json))
# print(r.text)

# jh = {'jk1':'jkuan1','jk2':'jkuan2','jk3':None}
# k = requests.get('http://httpbin.org/cookies', cookies=jh)
# print(k.text)
# jh = {'jk1':'jkuan1','jk2':'jkuan2','jk3':None}
# k = requests.post('http://httpbin.org/post', data=jh)
# print(k.text)
#
# from bs4 import BeautifulSoup
# from HTMLParser import HTMLParser
# import sqlite3

import requests
from lxml import etree


for id in range(0, 251, 25):
    r = requests.get('https://movie.douban.com/top250/?start=' + str(id))
    r.encoding = 'utf-8'
    print(r.content)
    print(len(r.content))
    # r.encoding = 'utf-8'
    # root = etree.HTML(r.content)
    # items = root.xpath('//ol/li/div[@class="item"]')

import requests
from bs4 import BeautifulSoup

movie_url = 'https://movie.douban.com/subject/1292052/'

def download_page(url):

	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
	}
	data = requests.get(url, headers = headers).content
	return data

def paser_html(html):
	soup = BeautifulSoup(html, 'lxml')




def main():
	print(paser_html(download_page(movie_url)))

if __name__ == '__main__':
	main()




















