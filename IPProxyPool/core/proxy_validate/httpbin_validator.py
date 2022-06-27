# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm
import time
import requests
from IPProxyPool.utils.http import get_request_headers

"""
实现代理池的校验模块：检查代理ip的 速度 和 匿名 程度；
匿名程度检查：如果响应的origin中有‘,’分割两个ip就是透明ip代理
如果响应的headers中含有Proxy-Connection 说明是匿名代理ip，否则就是高匿代理ip
检查是否支持https和http
"""

def check_http_proxies(prosies,is_http=True):
    if is_http:
        test_url='http://httpbin.org/get'
    else:
        test_url='https://httpbin.org/get'
    #获取开始时间
    start=time.time()
    #发送请求获取响应数据
    response=requests.get(test_url,headers=get_request_headers(),proxies=prosies)
