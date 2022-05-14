# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

vetor = []
tamanho = int(input())
n = input().split()

[vetor.append(int(numero)) for numero in n]

print(f'Menor valor: {min(vetor)}')
print(f'Posicao: {vetor.index(min(vetor))}')
