# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
num1 = int(linha[0])
num2 = int(linha[1])

if (num1%num2 == 0) or (num2%num1 == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
