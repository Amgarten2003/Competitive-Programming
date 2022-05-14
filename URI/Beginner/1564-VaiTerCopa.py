# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:
        x = int(input())
        if x > 0:
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError:
        break
