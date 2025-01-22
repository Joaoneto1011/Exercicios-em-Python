#crie um programa que leia o ano de nascimento de sete pessoas.
#no final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores

from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    ano_nascimento = int(input('Em que ano a {} pessoa nasceu?  '.format(c)))
    idade = ano_atual - ano_nascimento

    if idade <= 20:
        menores = menores + 1
        
    elif idade >= 21:
        maiores = maiores + 1

print('Ao todo temos {} pessoas que nao sao maiores de idade!'.format(menores))
print('Ao todo temos {} pessoas que ja sao maiores de idade!'.format(maiores))
