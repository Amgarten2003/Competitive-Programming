# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

soma = 0
contagem = 0

while True:
    user = int(input())
    if user < 0:
        break
    soma += user
    contagem += 1
print('{:.2f}'.format(soma / contagem))
