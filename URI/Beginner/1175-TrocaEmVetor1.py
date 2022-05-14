# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = []

for i in range(20):
    user = int(input())
    n.append(user)

n = n[::-1]
for index in range(len(n)):
    print(f'N[{index}] = {n[index]}')
