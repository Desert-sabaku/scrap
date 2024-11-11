import os
from typing import Optional

from scrapy import Spider
from scrapy.http import Response


class QuoteSpider(Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]

    # for mkdir dist. not necessary
    def __init__(self, name: Optional[str] = None):
        super().__init__(name)
        os.makedirs("dist", exist_ok=True)

    # def start_requests(self):
    #     urls = [
    #         "http://quotes.toscrape.com/page/1/",
    #         "http://quotes.toscrape.com/page/2/",
    #     ]

    #     for url in urls:
    #         yield Request(url=url, callback=self.parse)

    def parse(self, response: Response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
