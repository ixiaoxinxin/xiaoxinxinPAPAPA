# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.contrib.spiders import Rule,CrawlSpider
from scrapy.selector import Selector

class LagouSpider(Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [#这个名称不能写错，否则会识别不到url,d导致爬不到数据
        "https://www.lagou.com/zhaopin/ceshigongchengshi/",
        # "https://www.lagou.com/zhaopin/zidonghuaceshi/",
        # "https://www.lagou.com/zhaopin/gongnengceshi/",
        # "https://www.lagou.com/zhaopin/xingnengceshi/",
        # "https://www.lagou.com/zhaopin/ceshikaifa/",
        # "https://www.lagou.com/zhaopin/heiheceshi/",
        # "https://www.lagou.com/zhaopin/shoujiceshi/"
    ]
    def parse(self, response):
        #filename = response.url.split("/")[-2]#将最后一个地址作为文件名进行存储
        #open(filename,'wb').write(response.body)
        sel = Selector(response)
        sites = sel.xpath('//*[@id="s_position_list"]/ul')
        for site in sites :
            title = site.xpath('//*[@id="s_position_list"]/ul/li').extract()

            #link = site.xpath('a/@href').extract()
            #desc = site.xpath('text()').extract()

            #将中文抓取结果从Unicode转换成utf-8
            #http://blog.csdn.net/cc7756789w/article/details/46049369
            s = str(title).replace('u\'','\'')
            print s.decode("unicode-escape")
            #print title