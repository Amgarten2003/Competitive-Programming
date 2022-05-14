# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

valores_positivos = []
soma = 0

for i in range(6):
    valor = float(input())
    if (valor >= 0):
        soma += 1
        valores_positivos.append(valor)

media = sum(valores_positivos) / len(valores_positivos) 

print(f'{soma} valores positivos')
print('{:.1f}'.format(media))