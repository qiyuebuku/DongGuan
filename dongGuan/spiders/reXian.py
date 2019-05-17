# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongGuan import items
import urllib 


class RexianSpider(CrawlSpider):
    name = 'reXian'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/sheqing?page=']


    rules = (
        Rule(LinkExtractor(allow=r'sheqing\?page=\d+')),
        Rule(LinkExtractor(allow=r'/index\.php/sheqing/show\?id=\d+'), callback='parse_item'),
    )

    def parse_item(self, response):
        # return
        print(response.url)
        item = items.ReXianItem()
        raw_title = response.xpath('//td[@class="tit20px"]/text()')[0]
        item['rx_type'] =raw_title.re('\[(.*)\]')[0]
        item['rx_number'] =raw_title.re('\](.*)\:')[0]
        item['rx_title'] = raw_title.extract().split(":")[-1]
        item['rx_content'] = "".join(response.xpath('//td[@id="content1"]/text()').extract()).strip()
        item['proposer_id'] = response.xpath('//strong[@id="username1"]/text()').extract()[0]
        item['detailed_link'] = response.url
        yield item
