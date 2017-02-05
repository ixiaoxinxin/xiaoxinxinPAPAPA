# Scrapy settings for itzhaopin project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


BOT_NAME = 'jobInfo'

SPIDER_MODULES = ['jobInfo.spiders']
NEWSPIDER_MODULE = 'jobInfo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'itzhaopin (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'jobInfo.pipelines.JsonWithEncodingTencentPipeline': 300,
}

LOG_LEVEL = 'INFO'

