# -*- coding: utf-8 -*-
import scrapy
from dongGuan import items

class RexianSpider(scrapy.Spider):
    name = 'reXian2'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/sheqing?page={}'
    offset = 0
    start_urls = [url.format(offset)]

    def parse(self,response):
        # 获取响应文件所有帖子中的url链接
        link_list = response.xpath('//a[@class="tezi14"]/@href').extract()
        # print(link_list)
        # 遍历url将他们交给调度器，调度器入队列
        for link in link_list:
            link = 'http://wz.sun0769.com' + link
            yield scrapy.Request(link,callback=self.parse_item)
        # 如果页面没有到最后一页
        # 拼接新的url，获取下一个页面内容，
        # 并对页面内容再次进行解析
        if self.offset <= 1606:
            self.offset +=30
            url = self.url.format(self.offset)
            print(url)
            yield scrapy.Request(url,callback=self.parse)

    def parse_item(self, response):
        item = items.ReXianItem()
        raw_title = response.xpath('//td[@class="tit20px"]/text()')[0]
        print(raw_title.extract().split(":")[-1])
        item['rx_type'] =raw_title.re('\[(.*)\]')[0]
        item['rx_number'] =raw_title.re('\](.*)\:')[0]
        item['rx_title'] = raw_title.extract().split(":")[-1]
        item['rx_content'] = "".join(response.xpath('//td[@id="content1"]/text()').extract()).strip()
        item['proposer_id'] = response.xpath('//strong[@id="username1"]/text()').extract()[0]
        item['detailed_link'] = response.url
        yield item
