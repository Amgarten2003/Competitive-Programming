# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

soma = 0
x = int(input())
y = int(input())

if (x > y):
    aux = y
    y = x 
    x = aux 

for i in range(x, y+1):
    if (i % 13 != 0):
        soma += i

print(soma)