# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    detail_link = scrapy.Field()
    position_info = scrapy.Field()
    people_number = scrapy.Field()
    work_location = scrapy.Field()
    publish_time = scrapy.Field()

class DongGuanItem(scrapy.Item):

    title = scrapy.Field()
    number = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

class Douban250Item(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    content = scrapy.Field()
    info = scrapy.Field()

class SinaItem(scrapy.Item):
    # 大类标题和url
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()

    # 小类标题和url
    sub_title = scrapy.Field()
    sub_url = scrapy.Field()

    # 小类目录储存路径
    sub_filename = scrapy.Field()

    # 小类下的子链接
    son_url = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
    

class Images360Item(scrapy.Item):

    id = scrapy.Field()
    group_title = scrapy.Field()
    qhimg_url = scrapy.Field()
    qhimg_thumb_url = scrapy.Field()