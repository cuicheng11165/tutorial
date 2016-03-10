﻿import scrapy
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import Website



class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/artech/"]

    output_location = 'D:\\Crawl\\cnblog\\Artech\\'

    def parse(self, response):

        s = response.url.strip('/')
        pos = s.rfind("/")
        filename = self.output_location + s[pos + 1:len(s) - 1]
  
        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = scrapy.Selector(response)
        for url in response.xpath('//a/@href').extract():
            if(url.find('artech') > 0):
                yield scrapy.Request(url, callback=self.parse)
         