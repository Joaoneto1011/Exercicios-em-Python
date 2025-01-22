#crie um pacote chamado utilidadesCeV
#que tenha dois modulos internos chamados moedas e dado.
#transfira todas as funçoes utilizadas nos desafios 107, 108, 109 e 110
#para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda

preço = float(input('Digite o preço: '))

moeda.resumo(preço, 35, 22)
