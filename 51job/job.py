# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

#异步加载的数据爬取

import urllib.request,urllib.error
from urllib import parse
import re
import json
import chardet

def main():
    getData()

#设置url链接
def setURL(keywords,page):
    keywords=parse.quote(parse.quote(keywords))
    url = 'https://search.51job.com/list/040000,000000,0000,00,9,99,' + keywords + ',2,'+str(page)+'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    print(url)
    return url


#获取一个页面的源代码
def askURL(url):
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36'}
    request=urllib.request.Request(url,headers=head)
    response=urllib.request.urlopen(request)
    html=''
    html=response.read().decode('gbk')
    # print(html)
    return html

# 获取多个网页信息并进行解析
def getData():
    keywords=input('请输入你想了解的职位的关键字：')
    datalist=[]
    for i in range(0,3):
        url=setURL(keywords,i+1)
        html=askURL(url)
        data=re.findall(r"\"engine_jds\":(.+?),\"jobid_count\"",html)
        jsonobj=json.loads(data[0])
        for item in jsonobj:
            data=[]
            data.append(item['job_name'])
            data.append(item['company_name'])
            data.append(item['companytype_text'])
            data.append(item['providesalary_text'])
            data.append(item['workarea_text'])
            data.append(item['jobwelf'])#工作的详细情况
            data.append(item['updatedate'])#发布时间
            datalist.append(data)
    print(datalist)
    return datalist

# 从本地的html解析数据
# def getData():
#     file=open('../text/job.html','rb')
#     html=file.read().decode('gbk')
#     datalist=[]
#
#     data=re.findall(r"\"engine_jds\":(.+?),\"jobid_count\"",html)
#     jsonobj=json.loads(data[0])
#     for item in jsonobj:
#         data=[]
#         data.append(item['job_name'])
#         data.append(item['company_name'])
#         data.append(item['companytype_text'])
#         data.append(item['providesalary_text'])
#         data.append(item['workarea_text'])
#         data.append(item['jobwelf'])#工作的详细情况
#         data.append(item['updatedate'])#发布时间
#         datalist.append(data)
#
#     print(datalist)
#     return datalist




if __name__=='__main__':
    main()
    print('成功爬取数据！')