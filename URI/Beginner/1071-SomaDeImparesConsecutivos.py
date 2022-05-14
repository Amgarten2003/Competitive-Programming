# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

valor1 = int(input())
valor2 = int(input())
impares = []

if (valor1 > valor2):
    menor = valor2
    maior = valor1
else:
    menor = valor1
    maior = valor2

for i in range(menor+1, maior):
    if (i % 2 != 0):
        impares.append(i)

print(sum(impares))