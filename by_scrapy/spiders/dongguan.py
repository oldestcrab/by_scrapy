# -*- coding:utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from by_scrapy.items import DongGuanItem

class DongGuanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    # 每一页的匹配规则
    page_link = LinkExtractor(allow=(r'wz\.sun0769.*type=4'))
    # 每个帖子的匹配规则a
    content_link = LinkExtractor(allow=(r'question\/\d+\/\d+\.shtml'))

    rules = [
        Rule(page_link, process_links='deal_url', follow=True),
        Rule(content_link, callback='parse_content')
    ]

    def deal_url(self, links):
        # print(links)

        return links
        
    def parse_content(self, response):
        # print(response.url)
        item = DongGuanItem()
        try:
            item['title'] = response.xpath('//td[@width="1135"]/span[1]/text()').extract()[0].strip()
        except:
            item['title'] = ''
        # print(item['title'])
        try:
            item['number'] = response.xpath('//td[@width="1135"]/span[2]/text()').extract()[0].strip()
        except:
            item['number'] = ''
        # print(item['number']) 
        item['url'] = response.url
        # print(item['url'])
        img = response.xpath('//div[@class="textpic"]')
        if len(img) == 0:
           content = response.xpath('//td[@class="txt16_3"]/text()').extract()
        else:
           content = response.xpath('//div[@class="contentext"]/text()').extract()
        
        item['content'] = ''.join(x.strip() for x in content)
        # print(item['content'])
        
        yield item