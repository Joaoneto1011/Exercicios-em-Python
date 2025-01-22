#faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500

soma = 0
contador = 0
for c in range (1, 501):
    if (c % 2 != 0) and (c % 3 == 0):
        soma = soma + c
        contador = contador + 1
print('A soma entre todos os {} numeros impares e multiplos de 3 entre 1 e 500 é igual a {}'.format(contador, soma))