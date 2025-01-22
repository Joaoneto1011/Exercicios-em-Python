#escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de fibonacci.
#exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

N = int(input('Quantos termos voce quer mostrar? '))

primeiro_elemento = 0
segundo_elemento = 1

print('{} -> {}'.format(primeiro_elemento, segundo_elemento), end= '')
contador = 3
while contador <= N:
    contador = contador + 1
    terceiro_elemento = primeiro_elemento + segundo_elemento

    print('-> {}'.format(terceiro_elemento), end= '')

    primeiro_elemento = segundo_elemento
    segundo_elemento = terceiro_elemento

print(' -> FIM')
