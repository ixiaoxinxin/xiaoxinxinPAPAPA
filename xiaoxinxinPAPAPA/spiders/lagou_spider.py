# -*- coding: utf-8 -*-
from scrapy.spider import Spider
class LagouSpider(Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    srart_url = [
        "https://www.lagou.com/zhaopin/ceshigongchengshi/",
        "https://www.lagou.com/zhaopin/zidonghuaceshi/",
        "https://www.lagou.com/zhaopin/gongnengceshi/",
        "https://www.lagou.com/zhaopin/xingnengceshi/",
        "https://www.lagou.com/zhaopin/ceshikaifa/",
        "https://www.lagou.com/zhaopin/heiheceshi/",
        "https://www.lagou.com/zhaopin/shoujiceshi/"
    ]
    def parse(self, response):
        filename = response.url.split("/")[-2]#将最后一个地址作为文件名进行存储
        open(filename,'wb').write(response.body)