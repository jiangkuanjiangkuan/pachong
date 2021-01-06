#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xlwt
import re

alldata = []
book_datas = {}
count = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

for i in range(1,3):
    jk = (i-1)*20
    book1 ='https://book.douban.com/tag/编程?start='+str(jk)+'&type=T'
    data = requests.get(book1, headers=headers)
    # 获得页面信息
    data.encoding = 'gbk'
    soup = BeautifulSoup(data.content, 'html.parser')
    for i in soup.find_all('div', class_="info"):
        # 爬取parser========
        try:
            name = i.find("h2").get_text()

            time = i.find('div', class_='pub').get_text()

            score =float(i.find('span', class_='rating_nums').get_text())

            people = i.find('span', class_='pl').get_text()
            num2 = re.sub(r'\D+', "", people)
            print(str(count) + "=======" +num2)

            data = [count,name,score,people,time]
            alldata.append(data)
            count = count + 1
        except :
            print('craw failed')
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('ke_qq')
head = ['序号', '书名', '评分', '参与评论人数', '出版信息']  # 表头
for h in range(len(head)):
    sheet.write(0, h, head[h])  # 写入表头
i = 1
for list in alldata:
    j = 0
    for data in list:
        sheet.write(i, j, data)
        j += 1
    i += 1
book.save('豆瓣图书.xls')



