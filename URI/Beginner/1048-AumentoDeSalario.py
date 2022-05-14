# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

salario_antigo = float(input())

if (salario_antigo > 0) and (salario_antigo <= 400):
    print('Novo salario: {:.2f}'.format(salario_antigo + (salario_antigo * (15 / 100))))
    print('Reajuste ganho: {:.2f}'.format(salario_antigo * (15 / 100)))
    print('Em percentual: 15 %')

elif (salario_antigo >= 400.01) and (salario_antigo <= 800):
    print('Novo salario: {:.2f}'.format(salario_antigo + (salario_antigo * (12 / 100))))
    print('Reajuste ganho: {:.2f}'.format(salario_antigo * (12 / 100)))
    print('Em percentual: 12 %')

elif (salario_antigo >= 800.01) and (salario_antigo <= 1200):
    print('Novo salario: {:.2f}'.format(salario_antigo + (salario_antigo * (10 / 100))))
    print('Reajuste ganho: {:.2f}'.format(salario_antigo * (10 / 100)))
    print('Em percentual: 10 %')

elif (salario_antigo >= 1200.01) and (salario_antigo <= 2000):
    print('Novo salario: {:.2f}'.format(salario_antigo + (salario_antigo * (7 / 100))))
    print('Reajuste ganho: {:.2f}'.format(salario_antigo * (7 / 100)))
    print('Em percentual: 7 %')

else:
    print('Novo salario: {:.2f}'.format(salario_antigo + (salario_antigo * (4 / 100))))
    print('Reajuste ganho: {:.2f}'.format(salario_antigo * (4 / 100)))
    print('Em percentual: 4 %')
