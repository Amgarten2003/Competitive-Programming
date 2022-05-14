# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
hora_inicial = int(linha[0])
minuto_inicial = int(linha[1])
hora_final = int(linha[2])
minuto_final = int(linha[3])

hora_total = hora_final - hora_inicial

if (hora_total < 0):
    hora_total += 24

minuto_total = minuto_final - minuto_inicial

if (minuto_total < 0):
    minuto_total += 60
    hora_total -= 1
    if hora_total < 0:
        hora_total += 24

if (minuto_total == 0) and (hora_total == 0):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_total, minuto_total))