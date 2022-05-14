# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

maiorAB = (a+b+abs(a-b))/2
maiorBC = (maiorAB+c+abs(maiorAB-c))/2
print(f'{int(maiorBC)} eh o maior')