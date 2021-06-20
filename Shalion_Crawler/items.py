# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    url = scrapy.Field()
    price_amount = scrapy.Field()
    price_currency = scrapy.Field()
    keyword = scrapy.Field()

