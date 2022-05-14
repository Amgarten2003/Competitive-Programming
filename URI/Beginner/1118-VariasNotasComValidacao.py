# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def calcular_notas():
    contagem = 0
    soma_notas = 0
    while contagem < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            contagem += 1
            soma_notas += nota

    print('media = {:.2f}'.format(soma_notas / 2))

calcular_notas()

while True:
    print('novo calculo (1-sim 2-nao)')
    num = int(input())
    while num < 1 or num > 2:
        print('novo calculo (1-sim 2-nao)')
        num = int(input())

    if num == 1:
        calcular_notas()
    else:
        exit()
