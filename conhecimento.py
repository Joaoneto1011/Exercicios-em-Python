#operadores aritmeticos:
# soma(+), subtraçao(-), multiplicaçao(*), divisao(/), potenciaçao(**), divisao inteira(//), resto da divisao(%)

#ordem de precedencia das operaçoes:
# 1: ()
# 2: **
# 3: *, /, //, %
# 4: +, -

#para achar raiz quadrada so pegar o numero e fazer **(1/2), por exemplo 81 ** (1/2)
#para conversao de metros para centimetros é so fazer a quantidade de metros * 100, pois 1 metro = 100 centimetros
#para conversao de metros para milimetros é so fazer a quantidade de metros * 1000, pois 1 metro = 1000 milimetros
# use () para criar tuplas e nao podera mudar oque esta dentro pois sao imutaveis
# use [] para criar listas e podera alterar quando quiser pois elas sao mutaveis
# coloque .strip() na frente da entrada e ele tirara todos os espaços que o usuario escrever 
n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {0}, a multiplicaçao é {1} e a divisao é {2}'.format(s, m, d))
print('A divisao inteira é {} e a exponenciaçao é {}'.format(di, e))

#sobre cores no terminal
# numeros pra estilo (style), 0, 1, 4, 7
# 0 = none (nulo), 1 = bold(negrito), 4 = underline (sublinhado), 7 = negative (inverte de fundo pra letra e vice e versa)

# numeros pra cores do  texto (text), 30,31,32,33,34,35,36,37
# 30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = roxo, 36 = ciano, 37 = cinza

# numeros pra cores do background, cor de fundo (back), 40,41,42,43,44,45,46,47
# sao as mesmas ordem de cores do texto so muda os numeros
#codigo para colocar as cores \033[style; text; back m]

#o codigo from datetime import date, faz colocar a data atual dentro do codigo e ajustar para oque for preciso

S = 0
for c in range (0, 6):
    numero = int(input('Digite um numero: '))
    S = S + numero
print('A soma de todos os numeros foi {}'.format(S))
print('FIM')

#para saber se o numero é par, se o numero % 2 == 0, ele é par
#para saber se o numero é impar, se o numero % 2 != 0, ele é impar

from datetime import date

ano_atual = date.today().year
Ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - Ano_nascimento
#codigo para calcular baseado no ano atual

#usando esse exemplo resolvo o exercicio 53 mais facil

inverso = 'junto[::-1]' #isso faz com que começe da primeira letra da frase e vai ate a a ultima letra da frase, porem voltando de um em um

#na repetiçao while, enquanto a condiçao escrita for verdadeira, ela vai acontecendo dentro do comando, quando essa condiçao for falsa ele sai 
#na repetiçao for, voce usa sempre que souber ate onde vai a repetiçao, se nao souber, usa a repetiçao while

# AS TUPLAS SAO IMUTAVEIS, nao se pode mudar as tuplas ja definidas
# () parenteses sao para  as tuplas
# [] colchetes sao para as listas 
# {} chaves sao para os dicionarios
# AS LISTAS SAO MUTAVEIS, podem ser alteradas em qualquer momento do codigo

# O metodo append nas listas serve para adicionar itens na proxima posiçao, apos o ultimo item
# O metodo insert insere um item em qualquer posiçao que quiser, basta apenas informar em qual posiçao deseja inserir
# O comando del serve para eliminar um item escolhido da lista por indice
# O metodo pop remove o ultimo item da lista, mais pode ser passado um parametro de qual item excluir
# O metodo remove serve para eliminar um item da lista passando o nome do item como parametro ao inves do indice
# O metodo sort serve para ordenar os valores da lista em forma crescente
# para ordenar os valores da lista ao contrario, usa o metodo sort(reverse=True)
# O comando len serve para mostrar quantos elementos há na lista
# A funçao enumerate('Valor do codigo') a resposta mostra o indice e o valor de toda a lista
# Quando igualamos uma lista a outra b = a, e fazemos alteraçao em uma lista, altera nas duas
# Para fazermos apenas uma copia de uma lista com outra, usamos b = a[:]
#valores = list()
#for contador in range (0, 5):
    #valores.append(int(input('Digite um valor: ')))
#for c, v in enumerate(valores):
    #print(f'Na posiçao {c} encontrei o valor {v}')
#print('Cheguei ao final da lista')

#variavel.values() em dicionario retorna todos os valores do dicionario juntos
#variavel.keys() em dicionario retorna as chaves do dicionario
#variavel.items() em dicionario retorna as chaves e os valores do dicionario

#por exemplo um dicionario {'Nome Jogador': Joao}, 'Nome Jogador' seria a chave(keys) e o Joao seria o valor(values)
#e se pedir a funçao items() ira retornar 'Nome Jogador': Joao