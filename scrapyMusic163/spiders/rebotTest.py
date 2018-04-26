#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2018/4/16
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen



'''
robot协议
测试能否爬取链接
url robot文件地址
spiderUrl 需要测试的链接
'''
def testUrl(roboturl,spiderUrl):
    rp = RobotFileParser()
    rp.parse(urlopen(roboturl).read().decode('utf-8').split('\n'))
    print(rp.can_fetch('*', spiderUrl))

if __name__ == '__main__':
    testUrl("http://www.lotour.com/robots.txt",'http://www.lotour.com/')
    pass