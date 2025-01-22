#aprimore o desafio 093 para que ele funcione com varios jogadores.
#incluindo um sistema de vizualizaçao de detalhes do aproveitamento de cada jogador 

lista_jogadores = []
while True:
    total_gols_feitos = 0
    Nome_Jogador = str(input('NOME: '))
    Partidas_Jogadas = int(input('PARTIDAS JOGADAS: '))
    gols_por_partida = []

    for partida in range (1, Partidas_Jogadas + 1):
        gols_feitos = int(input(f'QUANTOS GOLS FEZ NA {partida + 1} PARTIDA: '))
        total_gols_feitos += gols_feitos
        gols_por_partida.append(gols_feitos)

    dicionario = {
        'Nome Jogador': Nome_Jogador,
        'Partida Jogadas': Partidas_Jogadas, 
        'Gols em Cada Partida': gols_por_partida,
        'Total De Gols Feitos': total_gols_feitos
    }
    lista_jogadores.append(dicionario.copy())

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

    while continuar not in 'SN':
        print('ERRO! Por favor responda S ou N')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if continuar == 'N':
        break

print('-='*30)

print('cod ', end='') #Imprime o título da primeira coluna, cod (código do jogador), sem pular para a próxima linha por causa do argumento end=''
for i in lista_jogadores[0].keys():#lista_jogadores[0] é o dicionário do primeiro jogador cadastrado.
#.keys() retorna as chaves do dicionário (exemplo: ['Nome Jogador', 'Partidas Jogadas', 'Gols em Cada Partida', 'Total De Gols Feitos']).
#Esse loop percorre todas as chaves e imprime cada uma delas como título das colunas.
    print(f'{i:<20}', end='')
print()
print('-='*30)

for k, v in enumerate(lista_jogadores):
    print(f'{k:>3} ',end='')
    for dado in v.values():
        print(f'{str(dado):<20}',end='')
    print()
print('-='* 30)

while True:
    opçao = int(input('Mostrar dados de qual jogador? (999 para parar):'))

    if opçao == 999:
        break
    if opçao >= len(lista_jogadores):
        print(f'ERRO! nao existe jogador com codigo {opçao}. tente novamente')
    else:
        jogador = lista_jogadores[opçao]
        print(f'-- LEVANTAMENTO DO JOGADOR {jogador["Nome Jogador"]}')
        for i, gols in enumerate(jogador['Gols em Cada Partida']):
            print(f'   => Na partida {i + 1}, fez {gols} gols')

print('<< VOLTE SEMPRE >> ')