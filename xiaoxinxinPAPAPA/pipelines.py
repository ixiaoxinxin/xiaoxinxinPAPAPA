# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient

from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MyCrawlerPipeline(object):
    def __init__(self):
        # 设置MongoDB连接
        client = MongoClient('MONGO_SERVER')#不设置端口就是用默认的  27017
        db = client[settings['MONGO_DB']]
        self.client = db[settings['MONGO_COLLECTION']]

    # 处理每个被抓取的MyCrawlerItem项
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:  # 过滤掉存在空字段的项
                valid = False
                raise DropItem("Missing {0}!".format(data))

        if valid:
            # 也可以用self.collection.insert(dict(item))，使用upsert可以防止重复项
            self.client.update({'url': item['url']}, dict(item), upsert=True)

        return item
