#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:
# 1 para binario, 2 para octal, 3 para hexadecimal

numero = int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversao: 
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input('Sua opçao: '))

if opçao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(numero, bin(numero)[2:]))

elif opçao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))

elif opçao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))

else:
    print('Opçao invalida, escolha uma das opçoes validas e tente novamente!')
