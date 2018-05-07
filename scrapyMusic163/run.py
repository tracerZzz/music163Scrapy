#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2018/4/28
from scrapy import cmdline


if __name__ == '__main__':
    # os.system("scrapy runspider music163Spider.py -o result.json")
    name = 'music163'
    # cmd = 'scrapy crawl {0} -o result.json'.format(name)
    cmd = 'scrapy crawl {0} '.format(name)
    cmdline.execute(cmd.split())
    pass