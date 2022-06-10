# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import urllib.error,urllib.request

def main():
    baseurl='https://www.qidian.com/finish/chanId21/'
    getData(baseurl)


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

    # for i in range(1,6):
    i=1
    url=url+str(r'-page'+str(i)+'/')
    html=askURL(url)
    #逐一解析数据
    soup=BeautifulSoup(html,'html.parser')
    novel=soup.select('.all-img-list cf')
    print(novel)


if __name__=='__main__':
    main()
    print("爬取成功！")