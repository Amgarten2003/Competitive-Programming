# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

lista = []

linha = input().split()
[lista.append(int(item)) for item in linha]

last_index = lista[len(lista)-1]
count = 0

for i in range(last_index):
    count = count + lista[0] + i

print(count)
