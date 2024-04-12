import scrapy
import unicodedata
import re


def get_slug_from_string(input_string, limit=None):
    normalized_string = unicodedata.normalize('NFD', input_string)
    stripped_string = ''.join(char for char in normalized_string if not unicodedata.combining(char))
    lowercase_string = stripped_string.lower()
    alphanumeric_string = re.sub(r'[^\w\s]', '', lowercase_string)
    slug_string = re.sub(r'\s+', '-', alphanumeric_string)
    
    if limit is not None:
        slug_string = slug_string[:limit].rstrip('-')
    
    return slug_string



class SmartupSpider(scrapy.Spider):
    name = "smartup"
   # allowed_domains = ["imdb.com"]
    #start_urls = ["https://technotesbr.blogspot.com"]
    start_urls = ["https://duquedecaxias.rj.gov.br"]

    def parse(self, response):
        for posts in response.css(".ot-articles-blog-list .item-content"):
            yield{
                'title' : posts.css('h2 a::text').get(),
                'data' : posts.css('.item-meta .item-meta-item::text').get(),
               'body' : posts.css('p::text').get(),
               'slug': get_slug_from_string(posts.css('h2 a::text').get(), limit=30)
            }
         