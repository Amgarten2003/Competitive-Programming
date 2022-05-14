# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

total_segundos = int(input())

qtd_horas = int(total_segundos / 3600)
total_segundos = total_segundos % 3600

qtd_minutos = int(total_segundos / 60)
total_segundos = total_segundos % 60

print('{}:{}:{}'.format(qtd_horas, qtd_minutos, total_segundos))