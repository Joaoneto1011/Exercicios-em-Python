#dentro do pacote utilidadesCeV que criamos no desafio 111
#temos um modulo chamado dado, crie uma funçao chamada leiaDinheiro()
#que seja capaz de funcionar como a funçao input()
#mas como uma validaçao de dados para aceitar apenas valores que sejam monetarios.

from utilidadesCeV import moeda
from utilidadesCeV import dado

preço = dado.LeiaDinheiro('Digite o preço: R$')

moeda.resumo(preço, 35, 22)