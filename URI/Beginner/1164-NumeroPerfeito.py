# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n_cases = int(input())
contagem = 0

while contagem < n_cases:
    contagem += 1
    n = int(input())
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma == n:
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')
