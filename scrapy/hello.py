aluno = str('Digite o nome do aluno: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
sum = n1 + n2
media = sum / 2


print(f'A soma {sum} e a media foi {media:.3f}')
print("A soma {}, a media {:.3f}".format(sum, media))

if media >= 6:
    print('APROVADO')
else:
    print('reprovado')