#melhore o jogo do desafio 028 onde o computador vai pensar em numero entre 0 e 10.
#so que agora o jogador vai tentar adivinhar ate acertar
#mostrando no final quantos palpites foram necessarios para vencer.

from random import randint

chances_tentadas = 0
computador = randint(0, 10) #faz o computador pensar, sortear um numero
print('Vou pensar em um numero entre 0 e 10. tente adivinhar')
acertou = False
while not acertou :
    jogador = int(input('Qual o seu palpite? '))
    chances_tentadas = chances_tentadas + 1
    
    if jogador == computador:
        print('Parabens, voce acertou e precisou de {} chances para acertar'.format(chances_tentadas))

    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')

        elif jogador > computador:
            print('Menos... tente mais uma vez.')
