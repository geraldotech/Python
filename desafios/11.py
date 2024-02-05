'''
Faça um programa que leia a largura e a altura de uma parede em metros calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
'''

lar = float(input('Largura da parede: '))
altura = float(input('Alturada da parede: '))

# area é a larg * alt
area = lar * altura

print(f'Sua parede tem a dimesão de {lar} x {altura} e sua área é de {area}m²')

tinta = area / 2;
print(f'Para pintar a parede é necessário {tinta}l de tinta.')