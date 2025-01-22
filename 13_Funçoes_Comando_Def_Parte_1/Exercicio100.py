#faça um programa que tenha uma lista chamada numeros
#e duas funçoes chamadas sorteia() e somaPar()
#a primeira funçao vai sortear 5 numeros e vai coloca-los dentro da lista.
#e a segunda funçao vai mostrar a soma entre todos os valores pares sorteados pela funçao anterior.

from random import randint
from time import sleep
lista_numeros = []
def sorteia ():
        print('-='*30)
        print(f'Sorteando 5 valores da lista: ', end='')
        for c in range(0, 5):
             n = randint(1, 10)
             lista_numeros.append(n)
             print(n, end=' ', flush=True)
             sleep(0.5)
        print('FIM')

def SomaPar():
    soma_pares = 0
    print(f'Somando os valores pares da lista {lista_numeros}, temos :', end=' ')
    for numero in lista_numeros:
        if numero % 2 == 0:
            soma_pares += numero
    print(soma_pares)

sorteia()
SomaPar()
print('FIM')
