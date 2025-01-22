#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

numero = int(input('Digite um numero qualquer: '))

if numero % 2 == 0:
    print('O numero {} é par'.format(numero))

else:
    print('O numero {} é impar'.format(numero))
