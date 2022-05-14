# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
x = int(linha[0])
y = int(linha[1])
count = 1

for i in range(1,(int((y/x))+1)):
    r = ""
    for y in range(3):
        r += str(count) + " "
        count += 1
    print(r[:-1])
