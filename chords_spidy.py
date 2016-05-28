# -*- coding: utf-8 -*-
import scrapy
import string
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from RandPlay.items import RandplayItem


class ChordsSpidySpider(CrawlSpider):
    name = 'chords-spidy'
    allowed_domains = ['put here domain']
    start_urls = ['put here starting url']

    rules = (
        Rule(LinkExtractor(allow=('\.html')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
		with open("chords/"+str(response.xpath('//title/text()').extract()), 'w') as f :
			f.write(response.body)
		i = RandplayItem()
		#titles = response.xpath('//title/text()').extract()
		#f = open("report1",'w')
		#print >> f , titles, '\n'
		#titles = response.xpath('//title/text()').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
		
		return i



