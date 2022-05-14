# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

vetor = []

while True:
    mary = 0
    john = 0
    n = int(input())
    if (n == 0):
        break
    else:
        linha = input().split()
        vetor = list(linha)
        for j in vetor:
            if (j == '0'):
                mary += 1
            else:
                john += 1
        print(f'Mary won {mary} times and John won {john} times')
