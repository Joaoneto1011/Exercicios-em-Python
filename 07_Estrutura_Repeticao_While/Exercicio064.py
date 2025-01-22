#crie um programa que leia varios numeros inteiros pelo teclado.
#o programa so vai parar quando o usuario digitar o valor 999, que é a condiçao de parada.
#no final, mostre quantos numeros foram digitados e qual foi a soma entre eles

numeros_digitados = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Digite um numero [999 para parar]: '))

    if numero != 999:
      numeros_digitados = numeros_digitados + 1
      soma = soma + numero

print('No total foram digitados {} numeros e a soma entre eles é de {}'.format(numeros_digitados, soma))