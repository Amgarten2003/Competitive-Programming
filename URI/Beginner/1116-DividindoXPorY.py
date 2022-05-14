# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    if (y == 0):
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(x/y))