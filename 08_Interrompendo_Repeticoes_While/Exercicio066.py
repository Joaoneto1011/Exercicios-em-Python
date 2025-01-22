#crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a condiçao de parada.
#no final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)

numeros_digitados = 0
soma = 0
numero = 0

while True:
    numero = (int(input('Digite um numero (999 para parar):  ')))
    if numero == 999:
        break

    numeros_digitados += 1
    soma += numero

  
print(f'foram digitados {numeros_digitados} numeros e a soma entre eles é de {soma}')