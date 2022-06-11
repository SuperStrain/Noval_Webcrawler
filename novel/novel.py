# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

#查找的数据有：小说名、作者、小说链接、类别、状态、简介、字数

from bs4 import BeautifulSoup
import urllib.error,urllib.request
import re

def main():
    baseurl='https://www.qidian.com/finish/chanId21/'
    getData(baseurl)


#定义查找小信息的关键字
findbkname=re.compile(r'<a data-bid=".*?" data-eid="qd_B58" href=".*?" target="_blank" title="(.*?)最新章节在线阅读">')
findlink=re.compile(r'<a data-bid=".*?" data-eid="qd_B58" href="(.*?)" target="_blank" title=".*?最新章节在线阅读">')
findwriter=re.compile(r'<a class="name" data-eid="qd_B59" href=".*?" target="_blank">(.*?)</a>')

#爬取一个网页的数据
def askURL(url):
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
    request=urllib.request.Request(url,headers=head)
    html=''
    response=urllib.request.urlopen(request)
    html=response.read().decode('utf-8')
    # print(html)
    return html

#爬取网页+解析数据
def getData(url):
    datalist=[]
    for i in range(1,2):
        rurl=url+str(r'-page'+str(i)+'/')
        html=askURL(rurl)
        #逐一解析数据
        soup=BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_="book-mid-info"):
            # print(item)
            datalist=[]  #建立列表保存一部小说的所有信息
            item=str(item)#变成字符串

            #添加小说名
            bookname=re.findall(findbkname,item)
            datalist.append(bookname)

            #添加作者名
            bookwriter=re.findall(findwriter,item)
            datalist.append(bookwriter)

            # 添加书的链接
            link=re.findall(findlink,item)[0]
            link='https:'+link
            datalist.append(link)

            #添加小说的类别




if __name__=='__main__':
    main()
    print("爬取成功！")