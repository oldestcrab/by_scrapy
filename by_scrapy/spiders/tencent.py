# -*- coding: utf-8 -*-
import scrapy
from by_scrapy.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']
    page = 0
    url = 'https://hr.tencent.com/position.php?&start='
    def parse(self, response):
        for each in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):
            item = TencentItem()
            try:
                item['name'] = each.xpath('td[1]/a/text()').extract()[0]
            except:
                item['name'] = ''
            try:
                item['detail_link'] = 'https://hr.tencent.com/' + each.xpath('td[1]/a/@href').extract()[0]
            except:
                item['detail_link'] = ''
            try:
                item['position_info'] = each.xpath('td[2]/text()').extract()[0]
            except:
                item['position_info'] = ''
            try:
                item['people_number'] = each.xpath('td[3]/text()').extract()[0]
            except:
                item['people_number'] = ''
            try:
                item['work_location'] = each.xpath('td[4]/text()').extract()[0]
            except:
                item['work_location'] = ''
            try:
                item['publish_time'] = each.xpath('td[5]/text()').extract()[0]
            except:
                item['publish_time'] = ''
            
            yield item
        
        if self.page < 3150:
            self.page +=10
        yield scrapy.Request(self.url+str(self.page), callback=self.parse)