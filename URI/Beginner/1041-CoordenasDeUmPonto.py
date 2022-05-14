# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
x = float(linha[0])
y = float(linha[1])

if (x == 0) and (y == 0):
    print('Origem')
elif (x == 0):
    print('Eixo Y')
elif (y == 0):
    print('Eixo X')
elif (x > 0) and (y > 0):
    print('Q1')
elif (x < 0) and (y > 0):
    print('Q2')
elif (x < 0) and (y < 0):
    print('Q3')
else:
    print('Q4')
