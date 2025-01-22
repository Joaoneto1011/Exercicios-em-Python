#a confederaçao nacional de nataçao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#ate 9 anos: mirim
#ate 14 anos: infantil
#ate 19 anos: junior
#ate 25 anos: senior
#acima de 20 anos: master

from datetime import date

ano_atual = date.today().year
Ano_nascimento = int(input('Digite a data de nascimento do atleta: '))
idade = ano_atual - Ano_nascimento

if idade <= 9:
    print('Esse atleta tem {} anos e esta na categoria MIRIM'.format(idade))

elif idade <= 14 and idade > 9:
    print('Esse atleta tem {} anos e esta na categoria INFANTIL'.format(idade))

elif idade <= 19 and idade > 14:
    print('Esse atleta tem {} anos e esta na categoria JUNIOR'.format(idade))

elif idade <= 25 and idade > 19:
    print('Esse atleta tem {} anos e esta na categoria SENIOR'.format(idade))

elif idade > 25:
    print('Esse atleta tem {} anos e esta na categoria MASTER'.format(idade))