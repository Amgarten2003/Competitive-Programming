# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

s = 0
j = 1
for i in range(1, 40, 2):
    s = float(s + i / j)
    j *= 2
print('{:.2f}'.format(s))
