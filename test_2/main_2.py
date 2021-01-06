#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time
import bookdownloader,bookpader,bookoutput,bookmanager
class domain(object):
    def __init__(self):
        self.book_urls = bookmanager.BookManger()#url管理器
        self.book_downloader = bookdownloader.BookDownloader()#html网页下载器
        self.book_parser = bookpader.BookPader() #html分析器
        self.book_output = bookoutput.BookOutput() #html输出器
    def craw(self,root_url):
        self.book_urls.add_newurl(root_url)
        try:
            url = self.book_urls.get_newurl()
            print('连接: %s' % (url))
            contents = self.book_downloader.book_downloader(url)
            data = self.book_parser.parser(url,contents)
            self.book_output.add_data(data)
            time.sleep(0.1)
        except:
            print('错误')
        self.book_output.out_data()

if __name__ == '__main__':
    root_url='https://book.douban.com/tag/编程?start=0&type=T'
    jk = domain()
    jk.craw(root_url)


#
# #
# #
# # import time
# # import urlmanager,htmldownloader,htmloutput,htmlparser
# # class DoubanMain(object):
# #     def __init__(self):
# #         self.urls = urlmanager.UrlManager() #url管理器
# #         self.downloader = htmldownloader.HtmlDownloader() #html网页下载器
# #         self.parder = htmlparser.HtmlParser()  #html分析器
# #         self.output = htmloutput.HtmlOutput()  #html输出器
# #
# #     def craw(self,root_url):
# #         count = 1
# #         self.urls.add_new_url(root_url)
# #         try:
# #             while self.urls.has_new_url():
# #                 new_url = self.urls.get_new_url() #从url管理器中获取一个未爬取的url
# #                 print('craw %d : %s' % (count, new_url))
# #                 html_cont = self.downloader.downloader(new_url)
# #                 new_urls, new_data = self.parder.paeser(new_url,html_cont)
# #                 self.urls.add_new_urls(new_urls)
# #                 self.output.collect_data(new_data)
# #                 time.sleep(0.1)
# #                 if count == 11:
# #                     break
# #                 count = count + 1
# #         except:
# #             print('craw failed')
# #         print(count)
# #         self.output.output_html()
# #
# # if __name__ == '__main__':
# #     root_url = "https://book.douban.com/subject/1477390/"
# #     jk = DoubanMain()
# #     jk.craw(root_url)