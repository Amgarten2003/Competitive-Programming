# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    linha = input().split()
    numero1 = int(linha[0])
    numero2 = int(linha[1])
    soma = 0
    if (numero1 <= 0) or (numero2 <= 0):
        break
    else:
        if (numero1 > numero2):
            aux = numero1
            numero1 = numero2
            numero2 = aux
        for i in range(numero1, numero2+1, 1):
            soma += i
            print(f'{i} ', end='')
        print(f'Sum={soma}')
