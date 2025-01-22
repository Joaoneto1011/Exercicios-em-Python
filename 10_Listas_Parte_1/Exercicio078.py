#faça um programa que leia 5 valores numericos e guarde-os em uma lista.
#no final, mostre qual foi o maior e o menor valor digitado e suas respectivas posiçoes na lista

lista = []
for numero in range (0, 5):
    lista.append(int(input(f'Digite um valor na posiçao {numero}: ')))

maior = max(lista)
menor = min(lista)
print('='*50)
print(f'Voce digitou os valores: {lista}')
print(f'O maior valor da lista é o numero {maior} nas posiçoes  ',end=' ')
for i, v in enumerate(lista):
    if lista[i] == maior:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor da lista é o numero {menor} nas posiçoes ',end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end=' ')
print()