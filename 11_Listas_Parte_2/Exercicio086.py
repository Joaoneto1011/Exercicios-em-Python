#crie um programa que crie uma matriz de dimensao 3x3 e preencha os valores lidos pelo teclado.
#no final, mostre a matriz na tela, com a formataçao correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Inicializa uma matriz 3x3 com zeros
# Preenchendo a matriz com valores do usuário
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

# Exibindo a matriz formatada
print("\nMatriz 3x3:")
for linha in matriz:
    for elemento in linha:
        print(f"[{elemento:^5}]", end="")  # Exibe cada elemento com alinhamento central
    print()