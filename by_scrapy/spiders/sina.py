# -*- coding:utf-8 -*-

import scrapy
from by_scrapy.items import SinaItem
import os

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allow_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []

        # 获取大类标题和url
        parent_title = response.xpath('//h3[@class="tit02"]/a/text()').extract()
        parent_url = response.xpath('//h3[@class="tit02"]/a/@href').extract()
        # print(parent_title, parent_url)

        # 获取小类标题和url
        sub_title = response.xpath('//ul[@class="list01"]/li/a/text()').extract()
        sub_url = response.xpath('//ul[@class="list01"]/li/a/@href').extract()
        # print(sub_title, sub_url)

        # 爬取大类
        for i in range(len(parent_title)):
            
            # 指定大类路径和路径名
            parent_filename = './data/' + parent_title[i]
            if not os.path.exists(parent_filename):
                os.makedirs(parent_filename)

            for j in range(len(sub_title)):
                item = SinaItem()

                # 保存大类title和url
                item['parent_title'] = parent_title[i]
                item['parent_url'] = parent_url[i]

                # 检查小类是否以大类url开头
                if_belong = sub_url[j].startswith(item['parent_url'])
                # print('=======')
                # 小类放入大类
                if if_belong:
                    sub_filename = parent_filename + '/' + sub_title[j]
                    # print(sub_filename)
                    if not os.path.exists(sub_filename):
                        os.makedirs(sub_filename)

                    item['sub_title'] = sub_title[j]
                    item['sub_url'] = sub_url[j]
                    item['sub_filename'] = sub_filename
                    
                    items.append(item)

            for item in items:
                yield scrapy.Request(url=item['sub_url'], meta={'meta_1':item}, callback=self.second_parse)

    def second_parse(self, response):
        meta_1 = response.meta['meta_1']
        son_urls = response.xpath('//a/@href').extract()
        # print(son_urls)
        items = []
        for i in range(len(son_urls)):
            if_belong = son_urls[i].startswith(meta_1['parent_url']) and son_urls[i].endswith('.shtml')
            if if_belong:
                item = SinaItem()
                item['parent_title'] =meta_1['parent_title']
                item['parent_url'] =meta_1['parent_url']
                item['sub_url'] = meta_1['sub_url']
                item['sub_title'] = meta_1['sub_title']
                item['sub_filename'] = meta_1['sub_filename']
                item['son_url'] = son_urls[i]
                items.append(item)
        for item in items:
            yield scrapy.Request(url=item['son_url'], meta={'meta_2':item}, callback=self.detail_parse)

    def detail_parse(self, response):
        item = response.meta['meta_2']
        title = response.xpath('//h1/text()').extract()[0]
        content_list = response.xpath('//div[@class="article"]/p/text()').extract()
        content = '\n'.join(content_list)
        item['head'] = title
        item['content'] = content

        yield item
