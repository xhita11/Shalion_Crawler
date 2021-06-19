# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.spiders import products_spider

class ShalionCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()
    price_amount = scrapy.Field()
    price_currency = scrapy.Field()
    keyword = scrapy.Field()

