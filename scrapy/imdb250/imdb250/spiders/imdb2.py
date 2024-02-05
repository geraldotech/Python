import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb2"
   # allowed_domains = ["imdb.com"]
    start_urls = ["https://technotesbr.blogspot.com"]

    def parse(self, response):
        for posts in response.css(".post-info"):
            yield{
                'title' : posts.css('.title-text::text').get(),
                'data' : posts.css('.post-date::text').get(), #because post-data is outside .title-text
            }
         