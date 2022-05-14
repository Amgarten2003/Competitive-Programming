# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

qtd_dias = int(input())

qtd_anos = int(qtd_dias / 365)
qtd_dias = qtd_dias % 365

qtd_meses = int(qtd_dias / 30)
qtd_dias = qtd_dias % 30

print(f'{qtd_anos} ano(s)')
print(f'{qtd_meses} mes(es)')
print(f'{qtd_dias} dia(s)')