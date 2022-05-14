# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    linha = input().split()
    valor1 = float(linha[0])
    valor2 = float(linha[1])
    valor3 = float(linha[2])
    media = ((valor1*2)+(valor2*3)+(valor3*5)) / 10
    print('{:.1f}'.format(media))