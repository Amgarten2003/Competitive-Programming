# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

qtd_perguntas = int(input())
lista = []

for i in range(qtd_perguntas):
    resposta = int(input())
    lista.append(resposta)

for i in range(len(lista)):
    print(f'resposta {i+1}: {lista[i]}')