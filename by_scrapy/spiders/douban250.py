# -*- coding:utf-8 -*-

import scrapy
from by_scrapy.items import Douban250Item

class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allow_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']
    start = 0
    end = '&filter='
# https://movie.douban.com/top250?start=0&filter=

    def parse(self, response):
        item = Douban250Item()

        movies = response.xpath('//div[@class="info"]')

        for each in movies:
            item['title'] = each.xpath('string(.//a)').extract()[0].strip().replace(' ','').replace('\n','')
            # print(item['title'])
            item['score'] = each.xpath('.//span[@class="rating_num"]/text()').extract()[0].strip()
            # print(item['score'])
            item['info'] = each.xpath('string(./div[@class="bd"]/p)').extract()[0].strip().replace('\n','').replace(' ','').replace('...','   ')
            # print(item['info'])
            try:
                item['content'] = each.xpath('.//span[@class="inq"]/text()').extract()[0].strip()
            except:
                item['content'] = ''

            yield item


        if self.start < 255:
            self.start += 25
            yield scrapy.Request('https://movie.douban.com/top250?start='+str(self.start)+self.end, callback=self.parse)
