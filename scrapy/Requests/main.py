import requests
import parsel
import json

url1 = 'https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MiZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhczpudWxsJkJ1c2NhVGVybW86bnVsbCZUaXBvRmlsdHJhZG89VG9kb3MmV29ya3NwYWNlSUQ6MTI2NSZrdF9kaWRheGlzPXRvcA==#'
url2 = 'https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?WorkspaceID=1260'

req = requests.get(url2)
sel = parsel.Selector(text=req.text)

# get status 
#print(req.status_code)
#print(parsel.Selector(text=req.text))

""" 
text = req.text
print(text) """


# get only txt add /text()
titulo = sel.xpath('//span[contains(@class,"sorting_title")]//h5/text()').getall()
print(titulo)
print(len(titulo))




#print(sel.xpath('//div[@class="container"]'))

""" nova url all cursos
thanks sel = parsel.Selector(text=req.text)
text = req.text
print(text)

https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?WorkspaceID=1260


//span[contains(@class, "sorting_title")] """