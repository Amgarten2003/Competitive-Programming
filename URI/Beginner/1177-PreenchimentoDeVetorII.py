# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

t = int(input())
count_t = 0
count = 0

for i in range(1000):
    print(f'N[{i}] = {count_t}')
    count_t += 1
    if count_t == t:
        count_t = 0
