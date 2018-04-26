# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapymusic163Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    link = scrapy.Field()  # 链接
    realLink=scrapy.Field() #完整连接
    desc = scrapy.Field()  # 简述
    listenCount = scrapy.Field() #播放数量
    posttime = scrapy.Field()  # 发布时间
    imgUrl=scrapy.Field()  # 歌单封面图片url
    # pass
