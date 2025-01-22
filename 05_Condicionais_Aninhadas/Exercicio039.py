#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar
#se é a hora de se alistar
#se ja passou do tempo do alistamento
#seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year
Ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - Ano_nascimento

print('Quem nasceu no ano {} tem {} anos em {}'.format(Ano_nascimento, idade, ano_atual))
if idade < 18:
    print('Voce ainda ira se alistar ao serviço militar, falta {} anos, espera sua hora!'.format(18 - idade))

elif idade == 18:
    print('Ja esta na hora de voce se alistar e comparecer ao serviço militar! ')

elif idade > 18:
    print('Ja passou {} anos do tempo do seu alistamento'.format(idade - 18))