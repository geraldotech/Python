import scrapy

url =  ["https://cursos.intelbras.com.br/app/catalogodecursos/catalogolista"]
url2 = ["https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?WorkspaceID=1260"]

class IntelbrascursosSpider(scrapy.Spider):
    name = "cursos"
    start_urls = url2

    def parse(self, response):
       for curso in  response.css('.sorting_title h5::text'):
           yield{
               'curso': curso.getall()
           }
