# -*- coding: utf-8 -*-
import scrapy

from scrapy.http.request import Request
from gunosynews.items import GunosynewsItem

class GunosySpider(scrapy.Spider):
    name = 'gunosy'
    allowed_domains = ['biglobe.ne.jp']
  
    start_urls = (
        'https://news.biglobe.ne.jp/',
    )

    def parse(self, response):
        for url in response.css("a::attr(href)").extract():
            if "http" not in url:
                yield Request("http:" + url)
            else:
                yield Request(url)

        yield { "title": response.css("title::text").extract()[0], "url": response.request.url }

        #for sel in response.css("div.nlst"):
        #    article = GunosynewsItem()
        #    article['url'] = sel.css("li.n-new > a::attr('href')").extract_first()
        #    article['title'] = sel.css(".n-new > a::text").extract_first()
        #    article['subcategory'] = sel.css("div.list_text > a::text").extract_first()
        #    yield article

        #next_page = response.css("div.page-link-option > a::attr('href')")
        #if next_page:
        #    url = response.urljoin(next_page[0],extract())
        #yield scrapy.Request(url, callback=self.parse)

        pass
