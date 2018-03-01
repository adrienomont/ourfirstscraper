# -*- coding: utf-8 -*-
import csv
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MultipleQuotesPaginationSpider(scrapy.Spider):
    name = "darty"
    allowed_domains = ["www.darty.com"]
    f = open("url_produit_darty.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()

    def parse(self, response):
        for article in response.css('div#produit'):
            item = {
               'title': article.css("div.product_name>span::text").extract(),
               'brand': article.css("a#darty_product_brand::text").extract(),
            #     'category': article.css(".infos_container>h3>a::text").extract(),
            #     # 'title': article.css(".infos_container>h2>a::text").extract(),
            #     'title': article.css("div.product_detail::attr(data-name)").extract(),
            #     'price': article.css(".darty_prix::text").extract(),
            }
            yield item

        # for page in response.css('div.darty_product_list_pages_list'):
        #     next_page_url = response.css('div.darty_product_list_pages_list>a::attr(href)').pop().extract()
        #     if next_page_url:
        #         next_page_url = response.urljoin(next_page_url)
        #         yield scrapy.Request(url=next_page_url, callback=self.parse)

        for page in response.css('div.darty_product_list_pages_list'):
            next_page_url = response.css('div.darty_product_list_pages_list>a::attr(href)').pop().extract()
            if next_page_url:
                next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(url=next_page_url, callback=self.parse)


        # for detail in response.css('div.infos_container'):
        #     next_detail_page_url = response.css('div.infos_container>h2>a::attr(href)').extract()
        #     if next_detail_page_url:
        #         next_detail_page_url = response.urljoin(next_detail_page_url)
        #         yield scrapy.Request(url=next_detail_page_url, callback=self.parse)


