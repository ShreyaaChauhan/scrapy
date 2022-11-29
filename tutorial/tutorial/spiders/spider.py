import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import TutorialItem
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst


class spider(CrawlSpider):
    name = "spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    base_url = "http://books.toscrape.com/"
    rules = [
        Rule(
            LinkExtractor(allow="catalogue/"), callback="parse_filter_book", follow=True
        )
    ]

    # def parse(self, response):
    #     all_books = response.xpath('//article[@class="product_pod"]')
    #     for book in all_books:
    #         book_url = book.xpath(".//h3/a/@href").extract_first()
    #         if "catalogue/" not in book_url:
    #             book_url = "catalogue/" + book_url
    #         book_url = response.urljoin(book_url)
    #         yield scrapy.Request(book_url, callback=self.parse_book)
    #     next_page_partial_url = response.xpath(
    #         '//li[@class="next"]/a/@href'
    #     ).extract_first()
    #     if next_page_partial_url:
    #         if "catalogue/" not in next_page_partial_url:
    #             next_page_partial_url = "catalogue/" + next_page_partial_url
    #         next_page_url = self.base_url + next_page_partial_url
    #         yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_filter_book(self, response):
        exists = response.xpath('//div[@id="product_gallery"]').extract_first()
        if exists:
            title = response.xpath("//div/h1/text()").extract_first()
            relative_image = (
                response.xpath('//div[@class="item active"]/img/@src')
                .extract_first()
                .replace("../..", "")
            )
            final_image = self.base_url + relative_image
            price = response.xpath(
                '//div[contains(@class, "product_main")]/p[@class="price_color"]/text()'
            ).extract_first()
            stock = (
                response.xpath(
                    '//div[contains(@class, "product_main")]/p[contains(@class, "instock")]/text()'
                )
                .extract()[1]
                .strip()
            )
            stars = (
                response.xpath('//div/p[contains(@class, "star-rating")]/@class')
                .extract_first()
                .replace("star-rating ", "")
            )
            description = response.xpath(
                '//div[@id="product_description"]/following-sibling::p/text()'
            ).extract_first()
            upc = response.xpath(
                '//table[@class="table table-striped"]/tr[1]/td/text()'
            ).extract_first()
            price_excl_tax = response.xpath(
                '//table[@class="table table-striped"]/tr[3]/td/text()'
            ).extract_first()
            price_inc_tax = response.xpath(
                '//table[@class="table table-striped"]/tr[4]/td/text()'
            ).extract_first()
            tax = response.xpath(
                '//table[@class="table table-striped"]/tr[5]/td/text()'
            ).extract_first()
            item = TutorialItem()
            item["title"] = title
            item["image"] = final_image
            item["price"] = price
            item["stock"] = stock
            item["stars"] = stars
            item["description"] = description
            item["upc"] = upc
            item["price_after_tax"] = price_excl_tax
            item["price_incl_tax"] = price_inc_tax
            item["tax"] = tax
            yield item

            # l = ItemLoader(item=TutorialItem())
            # l.add_value("title", title)
            # l.add_value("image", final_image)
            # l.add_value("stock", stock)
            # l.add_value("stars", stars)
            # l.add_value("description", description)
            # l.add_value("upc", upc)
            # l.add_value("price_after_tax", price_excl_tax)
            # l.add_value("price_incl_tax", price_inc_tax)
            # l.add_value("tax", tax)
            # return l.load_item()

            # product2 = item.deepcopy()
            # print(product2)
            # return item
            # yield {
            #     "Title": title,
            #     "Image": final_image,
            #     "Price": price,
            #     "Stock": stock,
            #     "Stars": stars,
            #     "Description": description,
            #     "Upc": upc,
            #     "Price after tax": price_excl_tax,
            #     "Price incl tax": price_inc_tax,
            #     "Tax": tax,
            # }
