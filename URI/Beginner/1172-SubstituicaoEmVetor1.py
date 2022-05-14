# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x = []
contagem = 0

while contagem <= 9:
    contagem += 1
    user = int(input())
    if user <= 0:
        x.append(1)
    else:
        x.append(user)

for i in range(len(x)):
    print(f'X[{i}] = {x[i]}')
    