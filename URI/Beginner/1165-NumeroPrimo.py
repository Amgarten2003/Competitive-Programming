# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    contagem = 0
    valor = int(input())
    
    for i in range(1, valor+1):
        if valor % i == 0:
            if i != 1 and i != valor:
                contagem -= 1
            else:
                contagem += 1

    if contagem == 2:
        print(f'{valor} eh primo')
    else:
        print(f'{valor} nao eh primo')
