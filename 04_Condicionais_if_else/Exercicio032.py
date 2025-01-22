#faça um programa que leia um ano qualquer e mostre se ele é bissexto

# esse import datetime é pra analisar o ano atual
from datetime import date
ano = int(input('Qual ano voce quer analisar? digite 0 para analisar o ano atual:  '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é um ano bissexto'.format(ano))

else:
    print('o ano {} nao é um ano bissexto'.format(ano))