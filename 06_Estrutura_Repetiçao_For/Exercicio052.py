#faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo

numero = int(input('Digite um numero: '))
total = 0
for c in range(1, numero + 1): #numero mais 1, porque o contador conta sempre ate um antes
    if numero % c == 0: #se o numero digitado pelo usuario for divisel por c, c é o contador que vai de 1 ate o numero digitado, o numero vai ficar amarelo
        print('\033[33m', end= ' ')
        total = total + 1 #se o numero for divisivel por c, o total vai receber mais 1
    else:
        print('\033[31m', end= ' ')# se o numero digitado pelo usuario nao for divisivel por c, o numero vai ficar vermelho
    print('{}'.format(c), end= ' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(numero, total), end= ' ')

if total == 2:
    print('\nE por isso ele é PRIMO')
else:
    print('\nE por isso ele nao é PRIMO')
