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

if (hora_inicial == hora_final) and (minuto_inicial == minuto_final):
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')

if (hora_inicial < hora_final) and (minuto_inicial < minuto_final):
    print(f'O JOGO DUROU {hora_final-hora_inicial} HORA(S) E {minuto_final-minuto_inicial} MINUTO(S)')
    
if (hora_inicial > hora_final) and (minuto_inicial > minuto_final):
    print(f'O JOGO DUROU {(hora_final+24)-hora_inicial} HORA(S) E {(minuto_final+60)-minuto_inicial} MINUTO(S)')
    
else:
    print(f'O JOGO DUROU 0 HORA(S) E {(minuto_final+60)-minuto_inicial} MINUTO(S)')
