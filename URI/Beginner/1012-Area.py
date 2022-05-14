# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha = input().split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])


print('TRIANGULO: {:.3f}'.format((a*c) / 2))
print('CIRCULO: {:.3f}'.format(3.14159 * (c**2)))
print('TRAPEZIO: {:.3f}'.format((a+b)*c / 2))
print('QUADRADO: {:.3f}'.format(b**2))
print('RETANGULO: {:.3f}'.format(b*a))
    