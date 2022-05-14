# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

precos = {1001:1.50, 1002:2.50, 1003:3.50, 1004:4.50, 1005:5.50}

n = int(input())
total = 0

for i in range(n):
    linha = input().split()
    pedido = int(linha[0])
    quantidade = int(linha[1])
    total += precos[pedido] * quantidade
print('{:.2f}'.format(total))