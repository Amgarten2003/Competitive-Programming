# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
soma = 0

for i in range(5):
    valor = int(input())
    if (valor % 2 == 0):
        soma += 1

print(f'{soma} valores pares')