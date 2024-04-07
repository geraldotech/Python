import requests
import parsel


url1 = 'https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?V29ya3NwYWNlSUQ9MTI2NSZjRmlsdHJvPSRNb2RvPWdyaWQmRmlsdHJvcyRQYWdpbmE6MiZQb3JQYWdpbmE6MjAmQ2F0ZWdvcmlhc0ZpbHRyYWRhczpudWxsJkJ1c2NhVGVybW86bnVsbCZUaXBvRmlsdHJhZG89VG9kb3MmV29ya3NwYWNlSUQ6MTI2NSZrdF9kaWRheGlzPXRvcA==#'
url2 = 'https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?WorkspaceID=1260'

req = requests.get(url1)
sel = parsel.Selector(text=req.text)
text = req.text
print(text)

#print(sel.xpath('//div[@class="container"]'))

""" nova url all cursos


https://cursos.intelbras.com.br/portal/layout/927/intelbras/home.asp?WorkspaceID=1260


//span[contains(@class, "sorting_title")] """