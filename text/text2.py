# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

# baseurl = 'http://fanfu.people.com.cn/'
# for i in range(0, 7):
#     baseurl = baseurl + str(r'/index' + str(i + 1) + '.html')
#     print(baseurl)
url='https://www.qidian.com/finish/chanId21/'
for i in range(1, 6):
    rurl = url + str(r'-page' + str(i) + '/')
    print(rurl)