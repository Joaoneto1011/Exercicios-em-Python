#faça um programa que tenha uma funçao chamada maior()
#que receba varios parametros com valores inteiros.
#seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
def maior(* num):
    valores = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for numero in num:
        print(f'{numero}', end=' ')
        valores += 1
    sleep(1)

    if len(num) > 0:
        print(f'foram informados {valores} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')

    else:
        print(f'Foram informados {valores} valores ao todo ')
        print('O maior valor informado foi 0')
maior(1,3,8,10,2,4)
maior(4,7,0)
maior(1,2)
maior(6)
maior()