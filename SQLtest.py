#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
import pymysql

if __name__ == '__main__':
    #打开数据库
    flag1 =0
    flag=3
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='rsxt')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    conn1 = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='jk')
    cursor1 = conn1.cursor(pymysql.cursors.DictCursor)
    if flag==3:
        sql = 'select * from yg'
        cursor.execute(sql)
        print(cursor.fetchall())
    if flag1==0:
        sql1 = 'insert into fensi(fensi_uname1,fensi_uage) values("jiangkuan", 24)'

        try:
            cursor1.execute(sql1)
            conn1.commit()
        except:
            conn1.rollback()
    if flag1 == 3:
        sql1 = 'select * from fensi'
        cursor1.execute(sql1)
        print(cursor1.fetchall())

    # cursor = conn.cursor()
    cursor.close()
    conn.close()

    cursor1.close()
    conn1.close()
