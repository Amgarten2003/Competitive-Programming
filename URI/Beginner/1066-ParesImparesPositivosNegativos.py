# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
soma_pares = 0
soma_impares = 0
soma_positivos = 0
soma_negativos = 0

for i in range(5):
    valor = int(input())
    if (valor > 0):
        soma_positivos += 1
    if (valor < 0):
        soma_negativos += 1
    if (valor % 2 == 0):
        soma_pares += 1
    if (valor % 2 != 0):
        soma_impares += 1
        
print(f'{soma_pares} valor(es) par(es)')
print(f'{soma_impares} valor(es) impar(es)')
print(f'{soma_positivos} valor(es) positivo(s)')
print(f'{soma_negativos} valor(es) negativo(s)')
