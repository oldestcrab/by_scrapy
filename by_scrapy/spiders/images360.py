# -*- coding:utf-8 -*-

import scrapy

class Images360Spider(scrapy.Spider):
    name = 'images360'
    allow_domains = ['image.so.com']
    part_url = 'https://image.so.com/zj?ch=beauty&listtype=new&temp=1'
    start_urls = 'https://image.so.com/zj?ch=beauty&listtype=new&temp=1'
    offset = 30
    # &sn=30

    def parse(self, response):
        print(response.text)
