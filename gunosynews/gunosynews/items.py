# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GunosynewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    subcategory = scrapy.Field()
     
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
