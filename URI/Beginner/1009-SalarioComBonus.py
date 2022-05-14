# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

nome = str(input())
salario = float(input())
vendas = float(input())
comissao = (vendas * (15 / 100))
total = salario + comissao
print('TOTAL = R$ {:.2f}'.format(total))