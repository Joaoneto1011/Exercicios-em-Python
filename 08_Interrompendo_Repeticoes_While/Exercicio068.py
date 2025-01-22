#faça um programa que jogue par ou impar com o computador.
#o jogo so sera interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint

computador = randint(0, 10)
jogador =  int(input('Digite um numero de 0 a 10: '))
escolha = str(input('Par ou Impar? [P/I]'))



