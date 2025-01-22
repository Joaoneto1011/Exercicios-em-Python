#crie um programa que gerencia o aproveitamento de um jogador de futebol.
#o programa vai ler o nome do jogador e quantas partidas ele jogou.
#depois vai ler a quantidade de gols feitos em cada partida.
#no final, tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o campeonato

total_gols_feitos = 0
Nome_Jogador = str(input('NOME: '))
Partidas_Jogadas = int(input('PARTIDAS JOGADAS: '))
gols_por_partida = []
for partida in range (1, Partidas_Jogadas + 1):
    gols_feitos = int(input(f'QUANTOS GOLS FEZ NA {partida} PARTIDA: '))
    total_gols_feitos += gols_feitos
    gols_por_partida.append(gols_feitos)

dicionario = {'Nome Jogador': Nome_Jogador,
              'Partida Jogadas': Partidas_Jogadas, 
              'Gols em Cada Partida': gols_por_partida,
              'Total De Gols Feitos': total_gols_feitos
              }
print('-='*30)
print(dicionario)
print('-='*30)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {Nome_Jogador} jogou {Partidas_Jogadas} partidas')
for i, v in enumerate(gols_por_partida):
    print(f'    => Na partida {i + 1}, fez {v} gols')
print(f'    => Totalizando {total_gols_feitos} gols feitos')