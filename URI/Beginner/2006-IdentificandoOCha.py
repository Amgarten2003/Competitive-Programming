# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

cha = int(input())
linha = input().split()
soma = 0
vetor_respostas = list(linha)

for i in vetor_respostas:
    if (i == str(cha)): 
        soma += 1

print(soma)