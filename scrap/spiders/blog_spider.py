import scrapy

from scrap.items import Posts


class BlogSpider(scrapy.Spider):
    name = "blog_spider"
    allowed_domains = ["www.zyte.com"]
    start_urls = ["https://www.zyte.com/blog/"]

    def parse(self, response):
        """
        レスポンスに対するパース処理
        """
        # css_grid_block = "Grid_grid__66sTK"
        css_card_block = "CardResource_card__uKf_5"
        css_title = "CardResource_link__4S2Jr"
        css_date_block = "CardResource_info__jdVxh"
        css_next_button = "Pagination_btnIcon__hc5oZ"

        for post in response.css(f".{css_card_block}"):
            # items に定義した Post のオブジェクトを生成して次の処理へ渡す
            yield Posts(
                url=post.css(f"a.{css_title}::attr(href)").get().strip(),
                title=post.css(f"a.{css_title}::text").get().strip(),
                date=post.css(f"div.{css_date_block} span::text").get().strip(),
            )

        # 再帰的にページングを辿るための処理
        older_post_link = response.css(f"a.{css_next_button}::attr(href)").get()
        if older_post_link is None:
            return

        # 次のページをのリクエストを実行する
        yield scrapy.Request(response.urljoin(older_post_link), callback=self.parse)
