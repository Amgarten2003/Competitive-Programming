# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x = int(input())
count = x
count2 = 0

while True:
    z = int(input())
    if z > x:
        break

while count <= z:
    x += 1
    count += x
    count2 += 1

print(count2+1)
