'''
leia um numero inteiro qualquer e mostre na tela a sua tabuada
'''

n = int(input('Digite um valor: '))

for i in range(1, 11):
    print(f'A tabuada: {n} x {i} = {n * i}')

