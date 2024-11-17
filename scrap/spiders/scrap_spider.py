# import datetime
import datetime
import os
from typing import Any, Optional
from urllib.parse import urlparse

import scrapy
from scrapy.http import Response


class ScrapSpider(scrapy.Spider):
    name = "scrap"
    allowed_domains = ["example.com"]
    start_urls = ["http://www.example.com"]
    max_depth = 2
    visited: set[str] = set()

    # TODO: Embedding Output Formats
    # custom_settings = {
    #     "FEEDS": {
    #         "dist/%(name)s_%(time)s.json": {
    #             "format": "json",
    #             "encoding": "utf8",
    #             "store_empty": False,
    #             "fields": None,
    #             "indent": 4,
    #             "overwrite": True,
    #         }
    #     },
    #     "FEED_URI_PARAMS": lambda: {
    #         "time": datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    #     }
    # }

    def __init__(self, name: Optional[str] = None, **kwargs: Any):
        super().__init__(name, **kwargs)
        os.makedirs("dist", exist_ok=True)

        # Processing of command line argument receipt
        if "url" in kwargs:
            self.start_urls = [kwargs["url"]]
            self.allowed_domains = [urlparse(kwargs["url"]).netloc]

        if "depth" in kwargs:
            self.max_depth = int(kwargs["depth"])

    def parse(self, response: Response, current_depth=0):
        self.visited.add(response.url)
        if current_depth >= self.max_depth:
            return

        links = []
        for anchor in response.xpath("//a"):  # type: ignore
            text = anchor.xpath("normalize-space(text())").get()
            link = response.urljoin(anchor.xpath("@href").get())

            if link not in self.visited:
                links.append((text, link))

        for text, link in links:
            yield {
                "text": text,
                "link": link,
                "depth": current_depth,
                "timestamp": datetime.datetime.now().isoformat(),
            }

        for _, link in links:
            yield scrapy.Request(
                link,
                callback=self.parse,
                cb_kwargs={"current_depth": current_depth + 1},
            )
