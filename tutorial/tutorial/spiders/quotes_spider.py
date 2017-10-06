import scrapy

"""
name identifies the Spider that crawls, and must be unique within projects

start_requests() returns an iterable of Requests, in this case a generator of
requests for each url in urls

parse() is called to handle the downloaded responses. It's an instance of
TextResponse that has the page content and methods to handle it
    Usually just parses the response and extracts the scraped data as dicts
    Also finds new URLs and generates new requests from them

Default callback response: parse()

scrapy crawl quotes | to run
"""

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    """
    Optional, default implementation only needs a list of start_urls
    def start_requests(self):
        urls = [
                'https://quotes.toscrape.com/page/1/',
                'https://quotes.toscrape.com/page/2/'
                ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)
    """    
    
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/1/'
            ]
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

   
