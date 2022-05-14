# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

soma_in = 0
soma_out = 0

n = int(input())

for i in range(n):
    valor = int(input())
    if (valor >= 10) and (valor <= 20):
        soma_in += 1
    else:
        soma_out += 1

print(f'{soma_in} in')
print(f'{soma_out} out')
