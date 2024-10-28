import os
from pathlib import Path
from typing import Any, Optional

from scrapy import Spider
from scrapy.http import Response


class QuoteSpider(Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]

    # for mkdir dist. not necessary
    def __init__(self, name: Optional[str] = None, **kwargs: Any):
        super().__init__(name, **kwargs)
        os.makedirs("dist", exist_ok=True)

    # def start_requests(self):
    #     urls = [
    #         "http://quotes.toscrape.com/page/1/",
    #         "http://quotes.toscrape.com/page/2/",
    #     ]

    #     for url in urls:
    #         yield Request(url=url, callback=self.parse)

    def parse(self, response: Response):
        PAGE = response.url.split("/")[-2]
        FILENAME = f"dist/quotes-{PAGE}.html"
        Path(FILENAME).write_text(response.text)
        self.log(f"Saved file {FILENAME}")
