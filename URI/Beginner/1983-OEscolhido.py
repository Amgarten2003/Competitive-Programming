# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
maior = 0
escolhido = 0

for i in range(n):
    linha = input().split()
    estudante = int(linha[0])
    nota = float(linha[1])
    if (nota >= maior):
        maior = nota
        escolhido = estudante

if (maior < 8):
    print('Minimum note not reached')
else:
    print(escolhido)