# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())
soma_total = 0
soma_coelhos = 0
soma_ratos = 0
soma_sapos = 0

for i in range(n):
    linha = input().split()
    if (linha[1] == 'C'):
        soma_total += int(linha[0])
        soma_coelhos += int(linha[0])
        
    elif (linha[1] == 'R'):
        soma_total += int(linha[0])
        soma_ratos += int(linha[0])
        
    else:
        soma_total += int(linha[0])
        soma_sapos += int(linha[0])
        
print(f'Total: {soma_total} cobaias')
print(f'Total de coelhos: {soma_coelhos}')
print(f'Total de ratos: {soma_ratos}')
print(f'Total de sapos: {soma_sapos}')
print('Percentual de coelhos: {:.2f} %'.format((soma_coelhos / soma_total)*100))
print('Percentual de ratos: {:.2f} %'.format((soma_ratos / soma_total)*100))
print('Percentual de sapos: {:.2f} %'.format((soma_sapos / soma_total)*100))