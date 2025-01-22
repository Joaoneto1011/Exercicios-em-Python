#adicione ao modulo moeda.py criado nos desafios anteriores
#uma funçao chamada resumo(), que mostre na tela algumas informaçoes
#geradas pelas funçoes que ja temos no modulo criado ate aqui.

from uteis import moedaspy

preço = float(input('Digite o preço: R$'))

moedaspy.resumo(preço, 70, 35)