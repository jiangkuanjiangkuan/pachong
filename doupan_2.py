#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# import time
# import requests
# from openpyxl import Workbook
# from bs4 import BeautifulSoup
#
# web = Workbook()
# sheet = web.active
# count = 1
# for i in range(0,100,25):
#     ret = requests.get('https://movie.douban.com/top250?start=%s&filter='%(i))
#     soup1 = BeautifulSoup(ret.text,'html.parser')
#     jk = soup1.find(name='jk',attrs={'class':'grid_view'})
#     li_list = jk.find_all_previous(name='li')
#     sheet.title = '电影好评'
#     sheet['A1'].value = '序号'
#     sheet['B1'].value = '电影名称'
#     sheet['C1'].value = '电影评分'
#     sheet['D1'].value = '电影连接'
#     sheet['E1'].value = '电影图片'
#     for li in li_list:
#         name = li.find(name='span',attrs={'class':'title'})
#         a = li.find(name='a')
#         span = li.find(name='span',attrs={'class':'rating_num'})
#         img = a.find(name='img')
#         count += 1
#         sheet['A%s' % (count)].value = count - 1
#         sheet['B%s' % (count)].value = name.text
#         sheet['C%s' % (count)].value = span.text
#         sheet['D%s' % (count)].value = a['href']
#         sheet['E%s' % (count)].value = img['src']
#     time.sleep(1)
#
# web.save('好评电影.xlsx')
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
web = Workbook()
sheet = web.active

def run(url):
    # 常用的浏览器请求头User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取ul
    ul = soup.find(name='ul', attrs={"class": "article"})
    # 获取所有的li
    li_list = ul.find_all(name='li')
    infos = []

    for li in li_list:

        sheet['A1'].value = 'title'
        sheet['B1'].value = 'href'
        sheet['C1'].value = 'info'

        name = li.find(name="h3")
        name1 = ""
        if name:
            name1 = (name.text)
        href = li.find(name='a')
        href1 = ""
        if href:
            href1 = ('http:' + href['href'])
        info = li.find(name='p')
        info1 = ""
        if info:
            info1 = (info.text)
        infos.append({"title": name1, "href": href1, "info": info1})
        for n in range(len(infos)):
            sheet['A%n'].write = name1
            sheet['B%n'].value.write = href1
            sheet['C%n'].value.write = info1
    print(infos)


if __name__ == '__main__':
    url = 'https://www.autohome.com.cn/news/'
    run(url)
    web.save('汽车之家.xlsx')