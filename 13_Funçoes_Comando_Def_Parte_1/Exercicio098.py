#faça um programa que tenha uma funçao chamada contador()
#que receba tres parametros: inicio, fim e passo e realize a contagem.
#seu programa tem que realizar tres contagens atraves da funçao criada.
#A) de 1 ate 10, de 1 em 1
#B) de 10 ate 0, de 2 em 2
#C) uma contagem personalizada

from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    
    if passo == 0:
        passo = 1


    print('-='*30)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')

    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('-='* 30)
print('Agora é sua vez de personalizar a contagem')
INICIO = int(input('INICIO: '))
FIM =    int(input('FIM: '))
PASSO =  int(input('PASSO: '))
contador(INICIO, FIM, PASSO)
