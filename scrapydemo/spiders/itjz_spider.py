import scrapy

class ItjzSpider(scrapy.Spider):
    name = "itjz"
    allowed_domains = ["itjuzi.com"]
    start_urls = [
        "http://itjuzi.com/company/16337"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)