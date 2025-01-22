#crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista.
#ja na posiçao correta de inserçao(sem usar o sort).
#no final mostre a lista ordenada na tela

lista_numeros = []

for c in range(0, 5):
    n = (int(input(f'Digite um numero: ')))
    if c == 0 or n > lista_numeros[-1]:
        lista_numeros.append(n)
        print('Adicionado ao final da lista')
    else:
        posiçao = 0
        while posiçao < len(lista_numeros):
            if n <= lista_numeros[posiçao]:
                lista_numeros.insert(posiçao, n)
                print(f'Adicionado na posiçao {posiçao} da lista')
                break
            posiçao += 1

print(f'Foram digitados os numeros {lista_numeros}')

#RESUMINDOOO, SO USAR O SORT KKKK