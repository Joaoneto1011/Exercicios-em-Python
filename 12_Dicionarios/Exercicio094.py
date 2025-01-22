#crie um programa que leia nome, sexo e idade de varias pessoas.
#guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
#no final, mostre:
#A) quantas pessoas foram cadastradas.
#B) a media de idade do grupo
#C) uma lista com todas as mulheres.
#D) uma lista com todas as pessoas com idade acima da media.

lista_acima_da_media = []
lista_mulheres = []
lista = []
soma_idade = 0
while True:
    nome = str(input('NOME: '))
    sexo = str(input('SEXO: [M/F]')).strip().upper()
    while sexo not in 'MF':
        print('Erro! Por favor digite apenas M ou F')
        sexo = str(input('SEXO: ')).strip().upper()
    idade = int(input('IDADE: '))

    dicionario = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
    lista.append(dicionario)

    soma_idade += idade

    if sexo in 'F':
        lista_mulheres.append(nome)

    continuar = str(input('Voce quer continuar? [S/N]')).strip().upper()
    
    while continuar not in 'SN':
        print('ERRO! Por favor responda apenas S ou N')
        continuar = str(input('Voce quer continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break

media_idade_grupo = soma_idade / (len(lista))

print('-='*30)
print(f'A) No total foram cadastradas {len(lista)} pessoas')
print(f'B) A media de idade do grupo é de {media_idade_grupo:.2f} anos')
print(f'C) A lista com todas as mulheres cadastradas é {lista_mulheres}')
print(f'D) A lista com as pessoas com idade acima da media do grupo é ', end='')

for pessoa in lista:
     if pessoa['Idade'] > media_idade_grupo:
        print('      ')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO!!')
