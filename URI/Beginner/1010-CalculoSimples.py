# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

linha1 = input().split()
codigo1 = int(linha1[0])
numero1 = int(linha1[1])
valor1 = float(linha1[2])

linha2 = input().split()
codigo2 = int(linha2[0])
numero2 = int(linha2[1])
valor2 = float(linha2[2])

total = (valor1 * numero1) + (valor2 * numero2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))