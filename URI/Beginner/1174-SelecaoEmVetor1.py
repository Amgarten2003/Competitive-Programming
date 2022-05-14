# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a = []

for i in range(100):
    user = float(input())
    a.append(int(user))
    if user <= 10.0:
        print(f'A[{i}] = {user}')
