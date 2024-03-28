from fpdf import FPDF


projeto = input('Digite a descrição do projeto: ')
horas_estimadas = input('Digite o total de horas estimadas: ')
valor_hora = input('Digite o valor da hora trabalhada: ')
prazo_estimado = input('Digite o prazo estimado: ')
valor_total_estimado = int(horas_estimadas) * int(valor_hora)


# In[23]:


#criando um pdf
pdf = FPDF()

pdf.add_page()
pdf.set_font('Arial')


# template
pdf.image("template.png", x=0, y=0)


pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))
# pdf.cell(w=0, h=5, txt="geraldox.com", border= 1, align="C", ln = 1)

pdf.multi_cell(w = 50, h=5, border = 1, txt= "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has")



#save
pdf.output('orcamento.pdf')
print('Orçamento gerado com sucesso')


# In[ ]:




