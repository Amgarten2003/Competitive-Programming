# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

vetor = []

for i in range(100):
    valor = int(input())
    vetor.append(valor)
        
maior = max(vetor)
print(maior)
print(vetor.index(maior)+1)