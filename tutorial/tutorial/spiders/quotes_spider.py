import scrapy
import logging


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        self.logger.info("Parse function called on %s", response.url)
        """
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
        anchors = response.css("ul.pager a")
        yield from response.follow_all(anchors, callback=self.parse)"""
