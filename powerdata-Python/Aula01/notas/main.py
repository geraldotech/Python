from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial')
pdf.set_font_size(23)
# image
pdf.image('template.jpg', x=0, y=0)

""" 
notaA = input('Digite nota A: ')
notaB = input('Digite nota B: ') """
notaA = '10'
notaB = "4"
soma = int(notaA) + int(notaB)



# template
pdf.text(150, 144, notaA)
pdf.text(150, 164, notaB)
pdf.text(150, 184, str(soma))
pdf.text(60, 290, 'created by Geraldo Filho')

# A4 page height (in mm)
page_height = 297





# save
pdf.output('output.pdf')
print('pdf gerarate sucess')