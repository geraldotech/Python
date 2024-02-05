'''
Algoritmo que leia o salario de um funcionario e mostre seu novo salário com 15% de aumento
'''


salario = float(input('Qual seu salario: '))
aumento = 15 * salario / 100
# modo 2 get 15% of a number
aumento2 = 800 * 115 / 100
print(f'Seu novo salario com 15% de aumento seria: {salario + aumento} - {aumento2}')