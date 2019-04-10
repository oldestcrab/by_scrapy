# -*- coding: utf-8 -*-
import scrapy
from by_scrapy.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']

    def parse(self, response):
        
        for each in response.xpath('//div[@class="li_txt"]'):
            # 实例化对象
            item = ItcastItem()

            item['name'] = each.xpath('h3/text()').extract()[0].strip()
            item['level'] = each.xpath('h4/text()').extract()[0].strip()
            item['info'] = each.xpath('p/text()').extract()[0].strip()

            yield item