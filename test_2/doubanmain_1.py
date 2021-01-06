#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import xlwt
import re
import time

# from flask_script import Manager,Server,Flask
# app = Flask(__name__)
# manager = Manager(app)
# manager.add_command("runserver", Server(use_debugger=True))

def downloader(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_12)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        htmldata = requests.get(url,headers=headers)
        htmldata.encoding = 'utf-8'
        # print(htmldata.text)
        soup = BeautifulSoup(htmldata.content,'lxml')
        # print(soup)
        url_booknum(soup)
    except:
        print("错误1")
# 找到书的url
def url_booknum(soup):
    try:
        new_book_urls = []
        for j in soup.find_all('div',class_="info"):
            book_urls = j.find_all('a', href=re.compile(r"https://book\.douban\.com/subject/\d+/$"))
            for book_url in book_urls:
                new_book_url = book_url['href']
                new_book_urls.append(new_book_url)
        data_book(new_book_urls)
    except:
        print("错误2")
        return None

# 爬取书信息
def data_book(new_book_urls):
    book_datas = {}
    # new_book_urls有问题？？？
    jk = new_book_urls
    print('cdfdfdf',jk)
    for j in range(len(new_book_urls)):
        if new_book_urls[j] is None:
            print('fndkhlbf')
            return None
        else:
            soup = downloader(new_book_urls[j])
            try:

                book_datas["序号"] = j+num+1
                print(book_datas["序号"])
                book_datas["链接"] = new_book_urls[j+1]
                print(book_datas["链接"])
                book_datas["书名"] = soup.find('span', property='v:itemreviewed').string
                print(book_datas["书名"])
                book_datas["评分"] = float(soup.find('strong', property="v:average").get_text())
                # print(book_datas["评分"])
                book_datas["参评人数"] = float(soup.find('span', property="v:votes").get_text())
                # print(book_datas["参评人数"])
                datas = soup.select('div > div.article > div.related_info > div.mod-hd > h2 > span.pl > a')
                book_datas["短评数"] = datas[0].text
                # print(book_datas["短评数"])
                datas = soup.select('div > div.article > div.related_info > section > header > h2 > span > a')
                book_datas["书评数"] = datas[0].text
                # print(book_datas["书评数"])
                book_datas["力荐度"] = soup.find('span', class_="rating_per").string

                xinxi = soup.find_all('div', id="info")
                book_datas["作者"] = re.findall(r'<a class href="(.*?)">(.*?)</a>',str(xinxi))
                # print(book_datas["作者"])
                book_datas["出版社"] = re.findall(r'<span class="pl">出版社:</span>(.*?)<br/>',str(xinxi))
                book_datas["出版年"] = re.findall(r'<span class="pl">出版年:</span>(.*?)<br/>',str(xinxi))
                book_datas["定价"] = re.findall(r'<span class="pl">定价:</span>(.*?)<br/>',str(xinxi))
                book_datas["ISBN"] =re.findall(r'<span class="pl">ISBN:</span>(.*?)<br/>',str(xinxi))

                study = soup.find_all('p',class_="pl")
                book_datas["读者数"] = re.findall(r'collections">(.*?)人读过</a>',str(study))
                if j > 10:
                    break
                if book_datas["评分"] is None or book_datas["短评数"] is None or book_datas["读者数"] is None or book_datas[
                    "力荐度"] is None:
                    print("没有数据1")
                    return None
                print(" print(count)", book_datas)
                time.sleep(5)
            except:
                print("错误3")
                return None

        if book_datas is None:
            print("没有数据2")
        book_data = [book_datas["序号"],book_datas["链接"],book_datas["书名"], book_datas["作者"], book_datas["评分"],book_datas["参评人数"],book_datas["短评数"],book_datas["书评数"],book_datas["读者数"],book_datas["力荐度"],book_datas["出版社"],book_datas["出版年"],book_datas["定价"],book_datas["ISBN"]]
        alldata.append(book_data)
        print("book_datas11111111111111", alldata)
        return alldata

if __name__ == '__main__':
    # manager.run()
    alldata = []
    for i in range(1, 10):
        time.sleep(5)
        num = (i - 1) * 20
        url = 'https://book.douban.com/tag/编程?start=' + str(num) + '&type=T'
        print(url)
        alldata =downloader(url)

    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('豆瓣图书-编程')
    head = ['序号',"链接",'书名',"作者", '评分',"参评人数", "短评数", "书评数","读者数","力荐度","出版社","出版年","定价","ISBN"]  # 表头
    for h in range(len(head)):
        sheet.write(0, h, head[h])  # 写入表头
    r = 1
    for list in alldata:

        l = 0
        for data in list:
            sheet.write(r, l, data)
            l += 1
        r += 1
    book.save('豆瓣图书-编程.xls')