# ÁREA DE TESTE DE CÓDIGOS

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

for i in range(n):
    soma = 0
    linha = input().split()
    numero1 = int(linha[0])
    numero2 = int(linha[1])
    if (numero1 > numero2):
        for i in range(numero1-1, numero2, -1):
            if (i % 2 != 0):
                soma += i
        print(soma)
    else:
        for i in range(numero1+1, numero2, 1):
            if (i % 2 != 0):
                soma += i
        print(soma)
