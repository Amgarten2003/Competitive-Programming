# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

total_alcool = 0
total_gasolina = 0
total_diesel = 0

while True:
    combustivel = int(input())
    if (combustivel == 1):
        total_alcool += 1
    if (combustivel == 2):
        total_gasolina += 1
    if (combustivel == 3):
        total_diesel += 1
    if (combustivel == 4):
        break

print('MUITO OBRIGADO')
print(f'Alcool: {total_alcool}')
print(f'Gasolina: {total_gasolina}')
print(f'Diesel: {total_diesel}')
