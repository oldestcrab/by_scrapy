# -*- coding:utf-8 -*-

import scrapy
import json
from by_scrapy.items import Images360Item

class Images360Spider(scrapy.Spider):
    name = 'images360'
    allow_domains = ['image.so.com']
    part_url = 'https://image.so.com/zj?ch=beauty&listtype=new&temp=1'
    start_urls = ['https://image.so.com/zj?ch=beauty&listtype=new&temp=1']
    offset = 30
    # &sn=30

    def parse(self, response):
        doc = json.loads(response.text)
        img_list = doc['list']
        for each in img_list:
            item = Images360Item()
            # print(each)
            item['id'] = each['id']
            # print(id)
            item['qhimg_url'] = each['qhimg_url']
            # print(qhimg_url)
            item['group_title'] = each['group_title']
            # print(group_title)
            item['qhimg_thumb_url'] = each['qhimg_thumb_url']
            # print(qhimg_thumb_url)

            yield item
        
        for i in range(3):
            next_url = self.part_url + '&sn=' + str((i+1)*self.offset)
            # print(next_url)

            yield scrapy.Request(next_url, callback=self.parse)