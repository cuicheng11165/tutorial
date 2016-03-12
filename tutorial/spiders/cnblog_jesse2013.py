import scrapy
import os
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import Website
from tutorial.crawlpolicysetting import outputlocation
from tutorial.pymssqlhelper import pymssqlhelper

class cnblog_jesse2013(scrapy.Spider):
    """description of class"""

    name = "jesse2013"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = ["http://www.cnblogs.com/"]
        
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

        if s.find('.') < 0 or s.find('?') > 0:
            return
        
        titlenodes = posttitle = response.xpath('/html/head/title/text()')
        if len(titlenodes) < 1:
            return

        posttitle = titlenodes[0].extract().encode('gb2312')
        
        pymssqlhelper.insertpage(response.url,self.name,str(posttitle),response.body.decode('utf8'))                          
        
        #return                                         
        sel = scrapy.Selector(response)
        for url in response.xpath('//a/@href').extract():
            if(url.find('cnblogs') > 0):
                yield scrapy.Request(url, callback=self.parse)
         