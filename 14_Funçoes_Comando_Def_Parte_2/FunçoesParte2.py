# CONTEUDO DA AULA

# INTERACTIVE HELP

print(input.__doc__)
help(input)
#existem essas duas formas para abrir a documentaçao/manual doque voce quer pesquisar.
#e estara escrito para oque serve a funçao pedida.

# DOCSTRING

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela;
    :parametro i: inicio da contagem
    :parametro f: fim da contagem
    :parametro p: passo da contagem
    :return: sem retorno
    Funçao criada por Joao neto
    """
    cont = i
    while cont <= f:
        print(f'{cont} ', end='')
        cont += p
    print('FIM')

contador(2, 10, 2)
help(contador)

#essas docstrings sao usadas para criar uma documentaçao de uma funçao que foi acabada de ser criada que ainda nao exista uma documentaçao.
#quando essa funçao for importada por alguem, a docstring(documentaçao colocada) aparecera para a pessoa.

#   PARAMETROS OPCIONAIS

def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de tres valores e mostra o resultado na tela;
    parametro a: o primeiro valor
    parametro b: o segundo valor
    parametro c: o terceiro valor
    Funçao criada por Joao neto.
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(b = 4, c = 2)
help(somar)

#parametro opcional, caso nao seja declarado nenhum numero na funçao chamada embaixo, o valor sera o parametro opcional passado na definiçao da funçao encima.


#   ESCOPO DE VARIAVEIS

def teste():
    N1 = 10
    print(f'N1 local vale {N1}')

N1 = 5
print(f'N1 global vale {N1}')
teste()


#   RETORNANDO VALORES

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

Resposta1 = somar(4, 3, 2)
Resposta2 = somar(3, 4)
Resposta3 = somar(2)

print(f'Os resultados foram {Resposta1}, {Resposta2}, {Resposta3}')


#  PARTE DE TREINAMENTO

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados sao {f1}, {f2}, {f3}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
if par(num):
    print('E par')
else:
    print('Nao é par')