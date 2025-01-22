#faça um programa que ajjude um jogador da MEGA SENA a criar palpites.
#o programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo
#cadastrando tudo em uma lista composta

from random import randint
from time import sleep
lista = []
jogos = []
print('-'* 30)
print('       JOGA NA MEGA SENA       ')
print('-'* 30)
quantidade = int(input('Quantos jogos voce quer que eu sorteie? '))
total_jogado = 1
while total_jogado <= quantidade:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogado += 1
print('-=' * 3, f' SORTEANDO {quantidade} JOGOS ', '-=' * 3)
for i, lista in enumerate(jogos):
    print(f'Jogo {i + 1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
