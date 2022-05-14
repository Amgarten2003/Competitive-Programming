# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

total_grenais = 1
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

while True:
    linha = input().split()
    gols_inter = int(linha[0])
    gols_gremio = int(linha[1])

    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_inter < gols_gremio:
        vitorias_gremio += 1
    else:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')
    novo_grenal = int(input())
    if novo_grenal == 1:
        total_grenais += 1
        pass
    else:
        print(f'{total_grenais} grenais')
        print(f'Inter:{vitorias_inter}')
        print(f'Gremio:{vitorias_gremio}')
        print(f'Empates:{empates}')
        if vitorias_inter > vitorias_gremio:
            print('Inter venceu mais')

        elif vitorias_inter < vitorias_gremio:
            print('Gremio venceu mais')

        else:
            print('Nao houve vencedor')
        exit()
