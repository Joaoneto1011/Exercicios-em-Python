#crie um programa que tenha uma funçao chamada voto().
#que vai receber como parametro o ano de nascimento de uma pessoa.
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleiçoes

def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade >= 18 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'

    elif idade < 16:
        return f'Com {idade} anos: NAO VOTA.'

    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'

print('-='* 20)

print(voto(2010))

print('-='*20)
print('Obrigado! volte sempre')
