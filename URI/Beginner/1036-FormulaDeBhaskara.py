# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import sqrt

linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

try:
    delta = b**2 - 4*a*c
    r1 = (-b + sqrt(delta)) / (2*a)
    r2 = (-b - sqrt(delta)) / (2*a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
except:
    print('Impossivel calcular')