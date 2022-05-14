# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    x = int(input())
    soma = 0
    contagem = 0

    if x == 0:
        break

    if x % 2 == 0:
        while contagem < 5:
            soma += x
            x = x + 2
            contagem += 1
    else:
        while contagem < 5:
            soma += x+1
            x = x + 2
            contagem += 1
    print(soma)
    soma = 0
