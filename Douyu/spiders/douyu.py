# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        print('begin start ---------------------%s'%response)
        douyu_data = json.loads(response.body)['data']
        for data in douyu_data:
            item = DouyuItem()
            item["vertical_src"] = data["vertical_src"]
            item["nickname"] = data["nickname"]
            print("+"*39)
            yield item

        if len(douyu_data) != 0:
            self.offset += 20
            yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)
