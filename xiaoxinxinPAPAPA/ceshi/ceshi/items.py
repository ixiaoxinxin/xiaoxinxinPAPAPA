# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CeshiItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass
class lagouItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    pass


