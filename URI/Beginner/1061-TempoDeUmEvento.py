# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def calculo_tempo():
  quatd_segundo1 = seg_1 + min_1*60 + hora_1*60*60 + data_inicio*60*60*24
  quatd_segundo2 = seg_2 + min_2*60 + hora_2*60*60 + data_final*60*60*24
  tempo_evento = quatd_segundo2 - quatd_segundo1

  data_total = tempo_evento // (60*60*24)
  hora_total1 = tempo_evento % (60*60*24)
  hora_total = hora_total1 // (60*60)
  min_total1 = hora_total1 % (60*60)
  min_total = min_total1 // (60)
  seg_total = min_total1 % (60)

  return seg_total, min_total, hora_total, data_total

data_inicio = int(input().split()[1])
hora_inicio = input().split()
hora_1 = int(hora_inicio[0])
min_1 = int(hora_inicio[2])
seg_1 = int(hora_inicio[4])

data_final = int(input().split()[1])
hora_final = input().split()
hora_2 = int(hora_final[0])
min_2 = int(hora_final[2])
seg_2 = int(hora_final[4])

resultado = calculo_tempo()

print(f'{resultado[3]} dia(s)')
print(f'{resultado[2]} hora(s)')
print(f'{resultado[1]} minuto(s)')
print(f'{resultado[0]} segundo(s)')