#refaça o exercicio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando o laço for

numero = int(input('Digite um numero para consultar sua tabuada: '))
for c in range (1, 11):
    print('{} x {} = {}'.format(numero, c, numero*c))
