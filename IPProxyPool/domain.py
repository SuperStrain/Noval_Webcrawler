# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

from settings import MAX_SCORE

#定义代理IP的数据类型

#1、定义Proxy类，继承object
class Proxy(object):
    #2、实现init方法，负责初始化，包含如下字段：
    def __init__(self,ip,port,protocol=-1,nick_type=-1,speed=-1,area=None,score=MAX_SCORE,diable_domains=[]):
        self.ip=ip
        self.port=port
        #代理支持的协议类型，http是0，https是1，都支持是2
        self.protocol=protocol
        #代理IP的匿名程度，高匿0，匿名1，透明2
        self.nick_type=nick_type
        self.speed=speed#单位是s
        self.area=area
        #代理IP的分数，衡量可用性
        self.score=score
        #不可用的域名列表
        self.diable_domains=diable_domains
    #3、提供str方法，返回数据字符串
    def __str__(self):
        #返回数据字符串
        return str(self.__dict__)