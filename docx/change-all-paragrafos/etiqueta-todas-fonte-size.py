from docx import Document
from docx.shared import Pt


documento = Document("ETIQUETA.docx")
#documento.add_heading('Document Title', 0)
#p = documento.add_paragraph('A plain paragraph having some ')
#p.add_run('bold').bold = True

nf = input('Nota fiscal:')
vendacasada = input('Num venda casada:')
origem = input('Num origem:')
destino = input('Num destino:')


referencias = {
   "xxxxxx": nf,
   "yyyyyyyy": vendacasada,
      "zzzz": origem,
  "kkkk": destino,
}


style = documento.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(30)

 


for paragrafo in documento.paragraphs:     
   for codigo in referencias:
      valor = referencias[codigo]      
      paragrafo.text = paragrafo.text.replace(codigo, valor) #.upper()
   for run in paragrafo.runs:
     run.font.size = Pt(30)
     
       
   

documento.save("etiqueta lançada.docx")

