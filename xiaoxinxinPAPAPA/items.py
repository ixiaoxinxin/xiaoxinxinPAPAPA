# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item, Field

class MyCrawlerItem(scrapy.Item):
    title = scrapy.Field()  # 文章标题
    url = scrapy.Field()  # 文章地址
    summary = scrapy.Field()  # 文章摘要
    pass

#
#Item封装了三个类对象
#
# class lagouItem(Item):
#     title = Field()
#     link = Field()
#     desc = Field()


