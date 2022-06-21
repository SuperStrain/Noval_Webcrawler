# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

import urllib.request,urllib.error
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3
#1、爬取数据 2、解析数据  3、保存数据
def main():
    baseurl='http://fanfu.people.com.cn/'
    # askURL(baseurl)
    datalist=getData(baseurl)
    e_path='news.xls'
    b_path='news.bd'
    # SaveToExcel(e_path,datalist)
    SaveToDB(b_path,datalist)


#定义查找小信息的关键字
findevent=re.compile(r'<a href=".*?/n1/2022/\d*/c.*?.html" target="_blank">(.*?)</a>')
findtime=re.compile(r'<i>\[(.*?)\]</i>')

#获取一个网页的数据
def askURL(url):
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36'}
    request=urllib.request.Request(url,headers=head)
    response=urllib.request.urlopen(request)
    html=''
    html=response.read().decode('gbk')
    # print(html)
    return html

#获取多个网页数据，并进行解析
def getData(baseurl):
    datalist=[]
    for i in range(0,7):
        url=baseurl+str(r'/index'+str(i+1)+'.html')
        html=askURL(url)

        #逐一解析数据
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.select('body > div > .fl > ul > li'):
            # print(item)
            data=[]
            item=str(item)

            #出现报错原因：list是空的，没有一个元素
            event=re.findall(findevent,item)
            if len(event)==0:
                data.append('')
            else:
                data.append(event[0])


            time = re.findall(findtime,item)[0]
            # time = time.replace('[','')
            # time = time.replace(']', '')
            # print(time)
            data.append(time)
            datalist.append(data)

    # print(datalist)
    return datalist

#将数据保存到Excel表格上
def SaveToExcel(path,datalist):
    workbook=xlwt.Workbook(encoding='utf-8')
    worksheet=workbook.add_sheet('sheet1')
    col=('新闻','发布时间')
    for i in range(len(col)):
        worksheet.write(0,i,col[i])
    for i in range(len(datalist)):
        print('正在打印第%d条新闻信息'%(i+1))
        data=datalist[i]
        for j in range(len(data)):
            worksheet.write(i+1,j,data[j])
    workbook.save(path)

#初始化数据库
def initDB(dbpath):
    sql='''
    create table news(
    id integer primary key autoincrement ,
    news text,
    time text
    )
    '''
    coon=sqlite3.connect(dbpath)
    cur=coon.cursor()
    cur.execute(sql)
    coon.commit()
    coon.close()
    print('建表成功！')

#保存数据到数据库
def SaveToDB(dbpath,datalist):
    initDB(dbpath)
    coon=sqlite3.connect(dbpath)
    cur=coon.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index]="'"+str(data[index])+"'"
        sql='''
        insert into news(
        news,time
        )
        values (%s,%s)
        '''%(data[0],data[1])
        cur.execute(sql)
        coon.commit()
    cur.close()
    coon.close()

if __name__=='__main__':
    main()
    print('成功爬取数据！')