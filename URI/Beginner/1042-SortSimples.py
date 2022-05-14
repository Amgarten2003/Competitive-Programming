# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
num1 = int(linha[0])
num2 = int(linha[1])
num3 = int(linha[2])

lista = [num1, num2, num3]
lista.sort()

for i in lista:
    print(i)

print('')

for i in linha:
    print(i)