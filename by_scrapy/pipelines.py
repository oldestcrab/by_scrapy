# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
from scrapy.conf import settings
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class ItcastPipeline(object):
    def __init__(self):
        self.file = open('./teachers.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

        return item

    def close_spider(self, spider):
        self.file.close()

class TencentJobPipeline(object):
    def __init__(self):
        self.file = open('./TencentJob_crawl.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

        return item

    def close_spider(self, spider):
        self.file.close()

class DongGuanPipeline(object):
    def __init__(self):
        self.file = open('./DongGuanWenZheng.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

        return item

    def close_spider(self, spider):
        self.file.close()

class Douban250Pipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']

        client = pymongo.MongoClient(host=host, port=port)

        mdb = client[dbname]

        self.post = mdb[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        data = dict(item)

        self.post.insert(data)

        return item

class SinaPipelines(object):

    def process_item(self, item, spider):
        son_url = item['son_url']
        # print(son_url)
        filename = son_url[7:-6].replace('/', '_') + '.txt'
        # print(filename)
        # print(item['sub_filename'])

        with open(item['sub_filename'] + '/' + filename, 'w', encoding='utf-8') as f:
            f.write(item['head'] + '\n')
            f.write(item['content'])

        return item

class Images360ImagePiples(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def get_media_requests(self, item, info):
        yield Request(item['qhimg_url'])

    def item_completed(self, results, item, info):
        # print(results)
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

class Images360MongoPiples(object):
    def __init__(self, host, port, dbname, post):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.post = post

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host =  crawler.settings.get('MONGODB_HOST'),
            port =  crawler.settings.get('MONGODB_PORT'),
            dbname =  crawler.settings.get('MONGODB_DBNAME_IMAGES360'),
            post =  crawler.settings.get('MONGODB_DOCNAME_IMAGES360')
        )

    def open_spider(self, spider):

        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.dbname]

    def process_item(self, item, spider):
        self.db[self.post].insert(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()