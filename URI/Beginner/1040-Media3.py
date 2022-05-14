# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
n1 = float(linha[0])
n2 = float(linha[1])
n3 = float(linha[2])
n4 = float(linha[3])

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10


if (media >= 7.0):
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')

elif (media < 5.0):
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')

else:
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: {:.1f}'.format(nota_exame))
    media_final = (media + nota_exame) / 2 
    if (media_final >= 5.0):
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(media_final))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(media_final))