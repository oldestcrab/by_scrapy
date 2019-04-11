# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from by_scrapy.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencentjob'
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "https://hr.tencent.com/position.php?&start=0"
    ]

    page = LinkExtractor(allow=(r'start=\d+'))
    
    rules = [
        Rule(page, callback="parse_content", follow= True)
    ]

    def parse_content(self, response):
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