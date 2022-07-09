# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

#定义MAX_SCORE=50,表示代理IP的默认最高分数
MAX_SCORE=50

#日志的配置信息
import logging
#默认的配置
LOG_LEVEL=logging.DEBUG  #默认等级
LOG_FMT='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
LOG_DATEFMT='%Y-%m-%d %H:%M:%S'#默认时间格式
LOG_FILENAME='log.log'#默认日志文件名称

#测试代理ip的超时时间
TEXT_TIMEOUT=50
