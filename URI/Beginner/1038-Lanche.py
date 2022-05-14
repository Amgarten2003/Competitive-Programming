# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

lista_itens = [4.00, 4.50, 5.00, 2.00, 1.50]

linha = input().split()
codigo = int(linha[0])
qtd = int(linha[1])

print('Total: R$ {:.2f}'.format(lista_itens[codigo-1]*qtd))