import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class ErrbackSpider(scrapy.Spider):
    name = "errback_example"
    start_urls = [
        "http://www.httpbin.org/",
        "http://www.httpbin.org/status/404",
        "http://www.httpbin.org/status/500",
        "http://www.httpbin.org:12345/",
        "https://example.invalid/",
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(
                u,
                callback=self.parse_httpbin,
                errback=self.errback_httpbin,
                dont_filter=True,
            )

    def parse_httpbin(self, response):
        self.logger.info("Got successful response from {}".format(response.url))

    def errback_httpbin(
        self, failure
    ):  # log all failures self.logger.error(repr(failure))
        # in case you want to do something special for some errors, # you may need the failure's type:
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware # you can get the non-200 response
            response = failure.value.response
            self.logger.error("HttpError on %s", response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error("DNSLookupError on %s", request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error("TimeoutError on %s", request.url)
