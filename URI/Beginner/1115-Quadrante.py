# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    linha = input().split()
    x = int(linha[0])
    y = int(linha[1])
    if (x == 0) or (y == 0):
        break
    else:
        if (x >= 0) and (y >= 0):
            print('primeiro')
        elif (x <= 0) and (y >= 0):
            print('segundo')
        elif (x <= 0) and (y <= 0):
            print('terceiro')
        else:
            print('quarto')