import scrapy
import os
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import Website
from tutorial.crawlpolicysetting import outputlocation
from tutorial.pymssqlhelper import pymssqlhelper

class cnblog_artech(scrapy.Spider):
    name = "artech"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/artech"]
        
    output_location = outputlocation + '\\' + name + '\\'

    

    def parse(self, response):
        s = response.url.strip('/')
        
        #do not save file that already exsit
        #do not save url that has ?(query)
        #

        #if s.find('?') < 0:
        #    pos = s.rfind("/")
        #    filename = self.output_location + s[pos + 1:len(s) - 1]
        #    if not os.path.exists(filename):
        #        with open(filename, 'wb') as f:
        #            f.write(response.body)

        
        
             
        titlenodes = posttitle = response.xpath('/html/head/title/text()').extract()
        if len(titlenodes) < 1:
            return

        #print titlenodes[0]
        #print type(titlenodes[0])

        #posttitle = titlenodes[0].encode('unicode')

        if s.find('.') > 0 and s.find('?') < 0:
            pymssqlhelper.insertpage(response.url,self.name,titlenodes[0],response.body.decode('utf8'))                          


        sel = scrapy.Selector(response)
        for url in response.xpath('//a/@href').extract():
            if(url.find(self.name) > 0):
                yield scrapy.Request(url, callback=self.parse)
         