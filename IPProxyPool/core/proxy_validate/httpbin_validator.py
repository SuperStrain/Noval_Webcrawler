# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm
import time
import requests
from IPProxyPool.utils.http import get_request_headers
from IPProxyPool.settings import TEXT_TIMEOUT
import json
from IPProxyPool.utils.log import logger
from IPProxyPool.domain import Proxy

"""
实现代理池的校验模块：检查代理ip的 速度 和 匿名 程度；
匿名程度检查：如果响应的origin中有‘,’分割两个ip就是透明ip代理
如果响应的headers中含有Proxy-Connection 说明是匿名代理ip，否则就是高匿代理ip
检查是否支持https和http
"""
def check_proxy(proxy):
    """
    用于检查指定 代理ip 响应速度 匿名程度 支持协议类型
    :param proxy:
    :return:检查后的代理ip模型对象
    """
    #准备代理ip字典
    proxies={
        'http':'http://{}:{}'.format(proxy.ip,proxy.port),
        'https':'https://{}:{}'.format(proxy.ip,proxy.port)
    }
    #测试代理ip
    http,http_nick_type,http_speed=check_http_proxies(proxies)
    https, https_nick_type, https_speed = check_http_proxies(proxies,False)
    # 代理支持的协议类型，http是0，https是1，都支持是2
    if https and http:
        proxy.protocol=2
        proxy.nick_type=https_nick_type
        proxy.speed=https_speed
    elif http:
        proxy.protocol=0
        proxy.nick_type=http_nick_type
        proxy.speed=http_speed
    elif https:
        proxy.protocol=1
        proxy.nick_type=https_nick_type
        proxy.speed=https_speed
    else:
        proxy.protocol=-1
        proxy.nick_type=-1
        proxy.speed=-1

    return proxy



def check_http_proxies(prosies,is_http=True):
    #代理IP的匿名程度，高匿0，匿名1，透明2
    nick_type = -1
    #响应速度，单位是s
    speed=-1
    if is_http:
        test_url='http://httpbin.org/get'
    else:
        test_url='https://httpbin.org/get'
    #获取开始时间
    start=time.time()
    #发送请求获取响应数据
    response=requests.get(test_url,headers=get_request_headers(),proxies=prosies,timeout=TEXT_TIMEOUT)
    try:
        if response.ok:
            #计算响应速度
            speed=round(time.time()-start,2)
            dic=json.loads(response.text)
            origin=dic['origin']
            proxy_connection=dic['headers'].get('Proxy-Connection',None)
            # 匿名程度检查：如果响应的origin中有‘, ’分割两个ip就是透明ip代理
            if ',' in origin:
                nick_type = 2
            # 如果响应的headers中含有Proxy-Connection
            elif proxy_connection:
                nick_type = 1
            # 说明是匿名代理ip，否则就是高匿代理ip
            else:
                nick_type = 0
            return True,nick_type,speed
        return False,nick_type,speed
    except Exception as ex:
        logger.exception(ex)
        return False,nick_type,speed

if __name__ == '__main__':
    proxy=Proxy('219.146.125.162',port='9091')
    print(check_proxy(proxy))