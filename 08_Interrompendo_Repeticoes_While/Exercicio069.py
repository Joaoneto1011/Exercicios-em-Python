#crie um programa que leia a idade e o sexo de varias pessoas.
#a cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. no final mostre: 
# A) quantas pessoas tem mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres tem menos de 20 anos.

maior_de_18 = 0
homens = 0
mulheres = 0
mulheres_menos_de_20 = 0
pessoas = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
    
    if idade > 18:
       maior_de_18 += 1

    if sexo == 'M':
         homens += 1

    if sexo == 'F':
        mulheres += 1

    if idade < 20 and sexo == 'F':
          mulheres_menos_de_20 += 1

    TotalPessoas = mulheres + homens
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Voce quer continuar? [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Temos {maior_de_18} pessoas com mais de 18 anos cadastradas')
print(f'Foram cadastrados no total {homens} homens e {mulheres} mulheres. Totalizando {TotalPessoas} pessoas cadastradas')
print(f'Foram cadastradas {mulheres_menos_de_20} mulheres com menos de 20 anos')