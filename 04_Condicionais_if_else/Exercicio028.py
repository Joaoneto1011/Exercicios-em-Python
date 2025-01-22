#escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5.
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# o programa devera escrever na tela se o usuario venceu ou perdeu

from random import randint

computador = randint(0, 5) #faz o computador pensar, sortear um numero
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')

jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar o numero que o computador pensou

if jogador == computador:
    print('Parabens! Voce conseguiu me vencer')

else:
    print('Ganhei! eu pensei no numero {} e nao no {}'.format(computador, jogador))
