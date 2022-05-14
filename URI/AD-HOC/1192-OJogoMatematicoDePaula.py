# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    linha = input()
    num1 = int(linha[0])
    letra = str(linha[1])
    num2 = int(linha[2])
    if (linha[1].upper()) and (num1 != num2):
        print(num2 - num1)
    elif (linha[1].lower()) and (num1 != num2):
        print(num1 + num2)
    else:
        print(num1 * num2)
