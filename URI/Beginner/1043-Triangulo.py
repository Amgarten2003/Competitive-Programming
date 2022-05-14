# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

if (a < b+c) and (b < a+c) and (c < a+b):
    print('Perimetro = {:.1f}'.format(a+b+c))
else:
    print('Area = {:.1f}'.format(((a+b)*c) / 2))