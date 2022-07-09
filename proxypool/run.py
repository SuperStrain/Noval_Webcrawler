# -*- codeing= utf-8 -*-
# @Time : 2022/5/15 11:12
# @Author : Yina
# @File : f.py
# @Software: PyCharm

from proxypool.scheduler import Scheduler
import argparse

parser=argparse.ArgumentParser(description='ProxyPool')
parser.add_argument('--processor',type=str,help='processor to run')
args=parser.parse_args()

if __name__ == '__main__':
    if args.processor:
        getattr(Scheduler(),f'run_{args.processor}')()
    else:
        Scheduler().run()

