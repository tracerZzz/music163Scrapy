#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2018/4/12


import scrapy
from scrapy import cmdline

from scrapyMusic163.items import Scrapymusic163Item

from scrapy_splash import SplashRequest
# from ..settings import DEFAULT_REQUEST_HEADERS
import parsel

# import codecs

class Music163Spider(scrapy.Spider):

    name = "music163"
    allowed_domains = ["163.com"]
    start_urls = [
        "https://music.163.com/discover/playlist/?order=new",
        "https://music.163.com/#/discover/playlist/"

    ]
    count =0

    def parse(self, response):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parseRequest,endpoint='render.json', args={'wait': 1,'html':1,'iframes': 1,'script':1})

    def parseRequest(self,response):
        iframe_html = response.data['childFrames'][0]['html']
        sel = parsel.Selector(iframe_html)
        # for se in sel.xpath('//div[@class="n-rcmd"]/div[@class="v-hd2"]/div[@class="tab"]/a'):
        for se in sel.xpath("//div[@id='cateListBox']/div[@class='bd']//a")[1:]:
            item = Scrapymusic163Item()
            item['title'] = se.xpath('text()')[0].extract()
            item['link'] = se.xpath('@href')[0].extract()
            url = response.urljoin(item['link'])
            yield SplashRequest(url,self.parse_gedan,endpoint='render.json', args={'wait': 2,'html':1,'iframes': 1,'script':1})
    def parse_gedan(self, response):
        iframe_html = response.data['childFrames'][0]['html']
        sel = parsel.Selector(iframe_html)
        for se in sel.xpath('//ul[@id="m-pl-container"]/li'):
            item = Scrapymusic163Item()
            item['title'] = se.xpath('p[@class="dec"]/a/text()')[0].extract()
            item['link'] = se.xpath('p[@class="dec"]/a/@href')[0].extract()
            url=response.urljoin(item['link'])
            item['realLink']=url
            item['listenCount']=se.xpath('div/div/span[@class="nb"]/text()')[0].extract()
            if(item['listenCount'] and "万" in item['listenCount']):
                item['listenCount']=int(item['listenCount'].replace("万","0000"))
            item['listenCount']=int(item['listenCount'])
            item['imgUrl']=se.xpath('div/img[@class="j-flag"]/@src')[0].extract()
            yield item
        next_pages = sel.xpath('//a[@class="zbtn znxt"]')

        if next_pages:
            url = response.urljoin(next_pages.xpath('@href')[0].extract())
            yield SplashRequest(url,self.parse_gedan,endpoint='render.json', args={'wait': 2,'html':1,'iframes': 1,'script':1})
if __name__ == '__main__':
    pass
