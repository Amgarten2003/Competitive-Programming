# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
valor1 = float(linha[0])
valor2 = float(linha[1])

if (valor1 > valor2):
    resultado = valor1 - valor2
    print('{:.2f}%'.format((resultado/valor1)*100))

else:
    resultado = valor2 - valor1
    print('{:.2f}%'.format((resultado/valor1)*100))