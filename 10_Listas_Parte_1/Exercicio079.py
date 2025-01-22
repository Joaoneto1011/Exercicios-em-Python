#crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
#caso o numero ja exista la dentro, ele nao sera adicionado.
#no final, serao exibidos todos os valores unicos digitados, em ordem crescente

lista_numeros = []

while True:
    numero = int(input('Digite qualquer valor numerico: '))

    if numero not in lista_numeros:
        lista_numeros.append(numero)
        print('Valor adicionado com sucesso')

    else:
        print('Esse numero ja existe na lista, tente outro numero!')

    continuar = str(input('Voce quer continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break

    while continuar not in 'SN':
        continuar = str(input('Voce quer continuar? [S/N]')).strip().upper()

lista_numeros.sort

print(f'Voce adicionou os numeros {lista_numeros} a lista')
