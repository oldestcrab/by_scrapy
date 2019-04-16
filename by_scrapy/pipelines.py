# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
from scrapy.conf import settings

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

