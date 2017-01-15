# -*- coding: utf-8 -*-
import scrapy


class MyCrawlerItem(scrapy.Item):
    title = scrapy.Field()  # 文章标题
    url = scrapy.Field()  # 文章地址
    summary = scrapy.Field()  # 文章摘要
    pass