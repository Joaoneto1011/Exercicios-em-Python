#crie um programa que vai ler varios numeros e colocar em uma lista.
#depois disso mostre:
#A) QUANTOS NUMEROS FORAM DIGITADOS
#B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE
#C) SE O VALOR 5 FOI DIGITADO E ESTA OU NAO NA LISTA.

lista_numeros = []
while True:
    numero = int(input('Digite qualquer numero: '))
    lista_numeros.append(numero)

    continuar = str(input('Quer continuar? [S/N]')).strip().upper()

    if continuar == 'N':
          break
    
    while continuar not in 'SN':
         continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    
lista_numeros.sort(reverse=True)

print(f'Foram digitados no total {len(lista_numeros)} numeros')
print(f'Os numeros da lista ordenados em forma decrescente sao: {lista_numeros}')

if 5 in lista_numeros:
     print('O numero 5 faz parte da lista')
else:
     print('O numero 5 nao foi encontrado na lista')