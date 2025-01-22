#faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio.
#indo de 10 ate 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Vamos la, o estouro dos fogos de artificio começara agora!!!')
for c in range (10, -1, -1):
    print(c)
    sleep (1)
print('BUUMM, o estouro foi um maximo!!!')