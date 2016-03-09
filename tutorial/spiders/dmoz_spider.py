import scrapy
from scrapy.spiders import Spider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from tutorial.items import Website


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = ["http://www.cnblogs.com/artech/"]

    rules = (Rule(SgmlLinkExtractor(allow=('myprogram/default.html\?page\=([\w]+)',),)),
        Rule(SgmlLinkExtractor(allow=('myprogram/p/',)), callback='parse_item'),
        Rule(SgmlLinkExtractor(allow=('myprogram/archive/',)), callback='parse_item'))

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

        sel = Selector(response)
        sites = sel.xpath('//a')
        items = []

        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            item = Website()
            item['name'] = title
            item['url'] = link
            items.append(item)
            print title, link, desc

        return items