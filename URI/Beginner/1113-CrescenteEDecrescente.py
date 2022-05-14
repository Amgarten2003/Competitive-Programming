# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    linha = input().split()
    num1 = int(linha[0])
    num2 = int(linha[1])
    if (num1 > num2):
        print('Decrescente')
    elif (num1 < num2):
        print('Crescente')
    else:
        break