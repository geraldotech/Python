'''
Fazer um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
'''

price = float(input('Qual valor do produto? '))
desconto = 5 * price / 100
print(f'Desconto de 5% {desconto}')
print(f'Novo valor com desconto: {price - desconto}')