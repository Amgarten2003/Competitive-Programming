# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

i = 0
j = 1
z = 0

while (i <= 2):
    while (z != 3):
        if i > 2.19:
            print('I={:.0f} J={:.0f}'.format(2, j))
        if i == 1.0 or i == 0 or i > 1.9:
            print('I={:.0f} J={:.0f}'.format(i, j))
        elif i < 2:
            print('I={:.1f} J={:.1f}'.format(i,j))
        j += 1
        z += 1
    j -= 3
    j += 0.2
    i += 0.2
    z = 0
