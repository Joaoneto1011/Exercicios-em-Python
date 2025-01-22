#crie um programa que crie uma matriz de dimensao 3x3 e preencha os valores lidos pelo teclado.
#no final, mostre a matriz na tela, com a formataçao correta.
#aprimore o desafio anterior, mostrando no final:
#A) a soma de todos os valores pares digitados.
#B) a soma dos valores da terceira coluna.
#C) o maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceiro_coluna = 0
maior_valor_segunda_linha = 0
for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}] [{coluna}]: '))

for linha in range (0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()

print(f'A soma de todos os valores pares é de {soma_pares}')

for linha in range (0, 3):
    soma_terceiro_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_terceiro_coluna}')

for coluna in range(0, 3):
    if coluna == 0:
        maior_valor_segunda_linha = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor_segunda_linha:
        maior_valor_segunda_linha = matriz[1][coluna]

print(f'O maior valor da segunda linha é o numero {maior_valor_segunda_linha}')
            