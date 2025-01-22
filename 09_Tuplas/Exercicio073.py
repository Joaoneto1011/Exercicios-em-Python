#crie uma tabela preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocaçao. depois mostre:
# A) apenas os 5 primeiros colocados.
# B) os ultimos 4 colocados na tabela.
# C) uma lista com os times em ordem alfabetica.
# D) em que posiçao na tabela esta o time do flamengo

tabela = ('BOTAFOGO', 'PALMEIRAS', 'INTERNACIONAL', 'FORTALEZA', 'FLAMENGO', 'SAO PAULO', 'CRUZEIRO', 'BAHIA', 'CORINTHIANS', 'ATLETICO-MG', 'VASCO', 'VITORIA', 'JUVENTUDE', 'GREMIO', 'ATHLETICO-PR', 'FLUMINENSE', 'CRICIUMA', 'BRAGANTINO', 'CUIABA', 'ATLETICO-GO')
print('-='*15)
print(f'Os 5 primeiros colocados sao: {tabela[0:5]}' )
print('-='*15)
print(f'Os 4 ultimos colocados na tabela sao: {tabela[-4:]} ')
print('-='*15)
print(f'A ordem alfabetica da tabela é: {sorted(tabela)} ')
print('-='*15)
print(f'O {tabela[4]} esta na 5 posiçao da tabela')
print('-='*15)