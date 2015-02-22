import scrapy
from pymongo import MongoClient

from pp.items import PPItem

class DmozSpider(scrapy.Spider):
    name = "pp"
    allowed_domains = ["pittsburghparent.com"]
    start_urls = [
        "http://www.pittsburghparent.com/Calendar/",
    ]

    def parse(self, response):
        for sel in response.xpath('//h3'):
            item = PPItem()
            item['link'] = sel.xpath('a/@href').extract()
            item['title'] = sel.xpath('a/text()').extract()
            print item['link']
            yield item
            print item['title']