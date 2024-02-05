from docx import Document

document = Document('old.docx')

dic = {
    'FULLNAME':'Geraldo Filho',
    'SURNAME':'First',
    'SURNAME2':'22',
  
}
for p in document.paragraphs:
    inline = p.runs
    for i in range(len(inline)):
        text = inline[i].text
        for key in dic.keys():
            if key in text:
                 text=text.replace(key,dic[key])
                 inline[i].text = text


document.save('new.docx')
