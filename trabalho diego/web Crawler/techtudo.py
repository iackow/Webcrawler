# -*- coding: utf-8 -*-
import scrapy


class TechtudoSpider(scrapy.Spider):
    name = 'techtudo'
    allowed_domains = ['www.techtudo.com.br']
    start_urls = ['http://www.techtudo.com.br/']

    def parse(self, response):
        pass
