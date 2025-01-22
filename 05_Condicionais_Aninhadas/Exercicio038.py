#escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior ou
#o segundo valor é maior ou
#nao existe valor maior, os dois sao iguais

valor1 = int(input('Digite o primeiro numero: '))
valor2 = int(input('Digite o segundo numero: '))

if valor1 > valor2:
    print('O primeiro valor {} é maior que o segundo valor {}'.format(valor1, valor2))

elif valor2 > valor1:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(valor2, valor1))

else:
    print('Nao existe valor maior, o primeiro valor {} e o segundo valor {} sao iguais'.format(valor1, valor2))