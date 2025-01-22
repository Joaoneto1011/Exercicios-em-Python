#adapte o codigo do desafio 107.
#criando uma funçao adicional chamada moeda().
#que consiga mostrar os valores como um valor monetario formatado.

from uteis import moedaspy

preço = float(input('Digite o preço: '))
print(f'A metade de {moedaspy.moeda(preço)} é {moedaspy.moeda(moedaspy.metade(preço))} ')
print(f'O dobro de {moedaspy.moeda(preço)} é {moedaspy.moeda(moedaspy.dobro(preço))}')
print(f'Aumentando 10%, temos {moedaspy.moeda(moedaspy.aumentar(preço))}')
print(f'Diminuindo 15%, temos {moedaspy.moeda(moedaspy.diminuir(preço, 15))}')