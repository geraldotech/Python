import scrapy


class SmartupSpider(scrapy.Spider):
    name = "smartup"
   # allowed_domains = ["imdb.com"]
    #start_urls = ["https://technotesbr.blogspot.com"]
    start_urls = ["https://duquedecaxias.rj.gov.br"]

    def parse(self, response):
        for posts in response.css(".ot-articles-blog-list .item-content"):
            yield{
                'title' : posts.css('h2 a::text').get(),
                #'data' : posts.css('.post-date::text').get(), #because post-data is outside .title-text
            }
         