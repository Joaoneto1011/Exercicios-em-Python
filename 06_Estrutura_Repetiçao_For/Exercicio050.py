#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
#se o valor digitado for impar, desconsidere-o.

SOMA = 0
CONTADOR = 0 
for c in range (1, 7):
    numero = int(input('Digite um numero: '))

    if numero % 2 == 0:
        SOMA = SOMA + numero
        CONTADOR = CONTADOR + 1

print('A soma dos {} numeros pares apresentados é igual a {}'.format(CONTADOR, SOMA))