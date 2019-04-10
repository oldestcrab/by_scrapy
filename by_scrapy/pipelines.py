# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

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
        self.file = open('./TencentJob.json', 'w', encoding='utf-8')
    
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(content)

        return item

    def close_spider(self, spider):
        self.file.close()