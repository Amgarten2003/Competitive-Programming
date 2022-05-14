# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
x = float(linha[0])  
y = float(linha[1])   
z = float(linha[2])  

valores = [x, y, z]
  
valores.sort(reverse=True)

a, b, c = valores[0], valores[1], valores[2]


if (a >= b+c):
    print('NAO FORMA TRIANGULO')
    exit()

if (a**2 == (b**2 + c**2)):
    print('TRIANGULO RETANGULO')

if (a**2 > (b**2 + c**2)):
    print('TRIANGULO OBTUSANGULO')

if (a**2 < (b**2 + c**2)):
    print('TRIANGULO ACUTANGULO')

if (a == b) and (b == c) and (c == a):
    print('TRIANGULO EQUILATERO')

if (a == b and c != a) or (b == c and a != b) or (c == a and b != c):
    print('TRIANGULO ISOSCELES')
