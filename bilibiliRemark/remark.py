# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

# 'https://api.bilibili.com/x/v2/reply/main?csrf=4cb2f8e3ab70964bf94bd639ba239832&mode=3&next=2&oid=927086822&plat=1&type=1'
# 'https://api.bilibili.com/x/v2/reply/main?csrf=4cb2f8e3ab70964bf94bd639ba239832&mode=3&next=4&oid=927086822&plat=1&type=1'
# 'https://api.bilibili.com/x/v2/reply/main?csrf=4cb2f8e3ab70964bf94bd639ba239832&mode=3&next=3&oid=927086822&plat=1&type=1'
import urllib.request,urllib.error
import re
import json
import sqlite3



def main():
    baseurl='https://api.bilibili.com/x/v2/reply/'
    datalist=getData(baseurl)
    Statistics_Sex(datalist)
    dbpath='remark.db'
    SaveToDB(datalist,dbpath)




#获取一个页面的html
def askURL(url):
    head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36'}
    request=urllib.request.Request(url,headers=head)
    response=urllib.request.urlopen(request)
    html=response.read().decode('utf-8')
    # print(html)
    return html

# 解析json格式的数据
def getData(baseurl):
    datalist=[]
    for i in range(0,30):
        url=baseurl+'main?csrf=4cb2f8e3ab70964bf94bd639ba239832&mode=3&next='+str(i+1)+'&oid=927086822&plat=1&type=1'
        html=askURL(url)
        data=re.findall(r"\"replies\":(.+?),\"top\"",html)#正则表达式获取关键信息
        # print(data)
        jsonobj=json.loads(data[0])#将str格式化为字典格式
        for item in jsonobj:
            data=[]

            # member=item['member']
            # content=item['content']
            # reply_control=item['reply_control']

            # 取出在字典里的字典（嵌套字典）----才可以调用键名，这是困扰我一个晚上的问题！
            data.append(item['member']['uname'])#添加用户id
            data.append(item['member']['sex'])#添加性别
            data.append(item['member']['sign'])#添加个性签名
            data.append(item['content']['message'])#评论
            data.append(item['reply_control']['time_desc'])#评论时间
            datalist.append(data)
    # print(datalist)
    return datalist

#数据库的初始化
def InitDB(path):
    coon=sqlite3.connect(path)
    cur=coon.cursor()
    sql='''
    create table remark(
    id integer primary key autoincrement,
    uname text,
    sex text,
    sign text,
    remark text,
    time text
    )
    '''
    cur.execute(sql)
    coon.commit()
    cur.close()
    coon.close()
    print('建表成功！')

#将数据存入数据库表格
def SaveToDB(datalist,path):
    InitDB(path)
    coon=sqlite3.connect(path)
    cur=coon.cursor()
    count=0
    for data in datalist:
        count=count+1
        for i in range(len(data)):
            data[i]="'"+str(data[i])+"'"
        sql='''
        insert into remark(
        uname,sex,sign,remark,time
        )
        values(%s,%s,%s,%s,%s) 
        '''%(data[0],data[1],data[2],data[3],data[4])
        cur.execute(sql)
        coon.commit()
        print('正在爬取第%d条评论信息'%count)
    cur.close()
    coon.close()
    print('bilibili评论信息已经全部保存至数据库！')

def Statistics_Sex(datalist):
    man=0
    woman=0
    unknown=0
    total=len(datalist)
    for data in datalist:
        if(data[1]=='男'):
            man=man+1
        elif(data[1]=='女'):
            woman=woman+1
        else:
            unknown=unknown+1
    man_=float(man)/float(total)
    woman_=float(woman)/float(total)
    unknown_=float(unknown)/float(total)
    print('评论人员性别分析：男性占比%.2f，女性占比%.2f，保密占%.2f,总共有%d人。'%(man_,woman_,unknown_,total))

if __name__=='__main__':
    main()
    print("爬取成功！")