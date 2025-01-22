#faça um programa que leia nome e peso de varias pessoas.
#guardando tudo em uma lista, no final mostre:
#A) quantas pessoas foram cadastradas
#B) uma listagem com as pessoas mais pesadas.
#C) uma listagem com as pessoas mais leves

lista_temporaria = []
lista_principal = []
maior_peso = menor_peso = 0
while True:
    lista_temporaria.append(str(input('Nome: ')))
    lista_temporaria.append(float(input('Peso: ')))
    if len(lista_principal) == 0:
        maior = menor = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior:
            maior = lista_temporaria[1]
        if lista_temporaria[1] < menor:
            menor = lista_temporaria[1]
    lista_principal.append(lista_temporaria[:])
    lista_temporaria.clear()

    continuar = str(input('Voce quer continuar? [S/N]')).strip().upper()

    while continuar not in 'SN':
        continuar = str(input('Voce quer continuar? [S/N]'))

    if continuar == 'N':
        break

print(f'No total foram cadastradas {len(lista_principal)} pessoas.')
print(f'O maior peso foi de {maior} Kg. Peso de ', end ='')
for pessoa in lista_principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor} Kg. Peso de ', end ='')
for pessoa in lista_principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
print()