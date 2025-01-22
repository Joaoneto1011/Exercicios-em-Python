#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#no final do programa, mostre:
#a media de idade do grupo
#qual é o nome do homem mais velho.
#quantas mulheres tem menos de 20 anos.

soma_idade = 0
media_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_20_anos = 0
for pessoa in range (1, 5):
    print('------- {} PESSOA -------'.format(pessoa))
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo, M/F: ')).strip().upper()
    soma_idade = soma_idade + idade

    if pessoa == 1 and sexo == 'M':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if idade > idade_homem_mais_velho and sexo == 'M':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if idade < 20 and sexo == 'F':
        mulheres_menos_20_anos = mulheres_menos_20_anos + 1

   
media_idade = soma_idade / 4
print('A media de idade do grupo é de {} anos'.format(media_idade))
print('A idade do homem mais velho é de {} anos e ele se chama {}'.format(idade_homem_mais_velho,nome_homem_mais_velho))
print('No total temos {} mulheres com menos de 20 anos'.format(mulheres_menos_20_anos))
