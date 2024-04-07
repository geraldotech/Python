# Scrapy

- [Scrapy DOCS](https://docs.scrapy.org/en/latest/topics/selectors.html)

Install the framework: `pip install scrapy`


- scrapy startproject <projectname/>
- cd <projectname>
- `scrapy genspider smartup smartup.com
- certificar que o  `smartup.py` foi criado pasta spiders

## Scrapy shell um ambiente de testes: 

> para sair: quit()

1. Enter shell: `scrapy shell`
2. Type: `fetch('https://technotesbr.blogspot.com')` or `scrapy shell site.com`

1. Type direct scrapy shell myurlhere.com


- Get Blog links `response.css('.post-title').getall()`
- Get Blog Links name `response.css(".title-text").get()`
- Get Only Links::text `response.css(".title-text::text").getall()`
- Get by id `response.css("#summary-component").get()`

- Associar a uma var and get len:

```python
links = response.css('.post-title').getall() 
len(links)

# 
links[2] #get link no index2
```

After script done:

- scrapy crawl <project>

Save:

- scrapy crawl imdb -O myfile.json - overwrite
- scrapy crawl imdb -o myfile.json - Notoverwrite
$ scrapy crawl smartup -O siteinfo.csv



# Intelbras

fetch("https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?WorkspaceID=1265")

- `fetch("https://cursos.intelbras.com.br/app/catalogodecursos/catalogolista")`
response.css(".product-img").get()

response.css(".link-produto").attrib["data-name"]
curso = response.css(".link-produto::attr(data-name)").getall()
curso = response.css("::attr(data-name)")
cursos = response.css(".titulo .link-produto::text").getall()


- [REF](https://www.youtube.com/watch?v=QdLgNr1mKQU)