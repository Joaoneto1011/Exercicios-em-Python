#modifique as funçoes que foram criadas no desafio 107.
#para que elas aceitem um parametro a mais.
#informando se o valor retornado por elas vai ser ou nao formatado pela funçao moeda().
#desenvolvida no desafio 108.

from uteis import moedaspy

preço = float(input('Digite o preço: '))

print(f'A metade de {moedaspy.moeda(preço)} é {(moedaspy.metade(preço, True))}')
print(f'O dobro de {moedaspy.moeda(preço)} é {(moedaspy.dobro(preço, True))}')
print(f'Aumentando em 10% o preço de {moedaspy.moeda(preço)}, temos {(moedaspy.aumentar(preço, 10, True))}')
print(f'Diminuindo em 15% o preço de {moedaspy.moeda(preço)}, temos {(moedaspy.diminuir(preço, 15, True))}')