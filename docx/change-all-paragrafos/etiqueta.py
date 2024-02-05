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



# Dictionaries
referencias = {
   "xxxxxx": nf,
   "yyyyyyyy": vendacasada,
   "zzzz": origem,
   "kkkk": destino,
}


#documento.add_paragraph('first item in ordered list')

for k, v in referencias.items():
    print(k, v)


for paragrafo in documento.paragraphs:     
   for codigo in referencias:  
      valor =  referencias[codigo] #.upper()  
      paragrafo.text = paragrafo.text.replace(str(codigo), str(valor)) #.upper()
     
      
      
   # font-size all para
   for run in paragrafo.runs:
      # run.startswith("Nota").underline = True
     print(run)
     run.font.size = Pt(16)
      #run.bold = True
     

## origem Destino
#paragrafo.runs[0].bold = True
#paragrafo.runs[0].underline = True


documento.save("etiqueta lançada.docx")

