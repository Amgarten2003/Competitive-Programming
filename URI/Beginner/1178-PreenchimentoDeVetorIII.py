# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = []
x = float(input())
x *= 2

for i in range(100):
    x /= 2
    n.append(x)
    print('N[{}] = {:.4f}'.format(i, x))
