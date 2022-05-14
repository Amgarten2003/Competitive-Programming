# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = []
t = int(input())

for i in range(10):
    n.append(t)
    t *= 2

for indice,valor in enumerate(n):
    print('N[{}] = {}'.format(indice, valor))
