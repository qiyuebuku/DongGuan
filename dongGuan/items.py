# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ReXianItem(scrapy.Item):
    rx_type = scrapy.Field()
    rx_number = scrapy.Field()
    rx_title = scrapy.Field()
    rx_content = scrapy.Field()
    proposer_id = scrapy.Field()
    detailed_link = scrapy.Field()