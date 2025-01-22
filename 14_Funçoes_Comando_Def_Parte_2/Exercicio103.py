#faça um programa que tenha uma funçao chamada ficha()
#que receba dois parametros opcionais:
#o nome de um jogador e quantos gols ele marcou.
#o programa devera ser capaz de mostrar a ficha do jogador.
#mesmo que algum dado nao tenha sido informado corretamente.

def ficha(nome_jogador="<desconhecido>", gols_marcados= 0):
    print('-='* 20)
    print(f'O jogador {nome_jogador} fez {gols_marcados} gol(s) no campeonato. ')

jogador = str(input('Nome Jogador: ')).strip()
gols = str(input('Numero de Gols: ')).strip()


if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if jogador == '':
    ficha(gols_marcados= gols)

else:
    ficha(nome_jogador=jogador, gols_marcados=gols)

