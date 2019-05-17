# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DongguanPipeline(object):
    def process_item(self, item, spider):
        return item

class ReXianPipeline(object):
    def __init__(self):
        self.f = open('ReXian.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        # print('正在写入……')
        self.f.write(json.dumps(dict(item), ensure_ascii=False))
        self.f.write("\n")
        return item
