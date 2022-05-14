# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí    
'''

n = int(input())

for i in range(n):
    valor = int(input())
    if (valor == 0):
        print('NULL')
    
    elif (valor % 2 != 0):
        if (valor > 0):
            print('ODD POSITIVE')
        else:
            print('ODD NEGATIVE')
    
    else:
        if (valor > 0):
            print('EVEN POSITIVE')
        else:
            print('EVEN NEGATIVE')