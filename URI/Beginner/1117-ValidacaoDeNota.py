# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

soma_loop = 0
soma_nota = 0

while (soma_loop != 2):
    nota = float(input())
    if (nota < 0) or (nota > 10):
        print('nota invalida')
    else:
        soma_loop += 1
        soma_nota += nota

print('media = {:.2f}'.format(soma_nota/2))