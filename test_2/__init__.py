#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#
#
# import requests
# import re
# from bs4 import BeautifulSoup
# from distutils.filelist import findall
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
# }
#
# page = 'http://movie.douban.com/top250?format=text'
# jk = requests.get(page,headers=headers)
# # print(contents)
# soup = BeautifulSoup(jk.content, "html.parser")
# print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
# for tag in soup.find_all('div', class_='info'):
#     # print tag
#     m_name = tag.find('span', class_='title').get_text()
#     m_rating_score = float(tag.find('span', class_='rating_num').get_text())
#     m_people = tag.find('div', class_="star")
#     m_span = m_people.findAll('span')
#     m_peoplecount = m_span[3].contents[0]
#     m_url = tag.find('a').get('href')
#     print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)
#爬虫爬取豆瓣书目录

