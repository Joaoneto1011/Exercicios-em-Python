#crie um modulo chamado moeda.py.
#que tenha as funçoes incorporadas aumentar(), diminuir(), dobro() e metade().
#faça tambem um programa que importe esse modulo e usa algumas dessas funçoes.

from uteis import moedaspy

preço = float(input('Digite o preço: R$'))

print(f'O dobro de {preço} é {moedaspy.dobro(preço)}')
print(f'A metade de {preço} é {moedaspy.metade(preço)}')
print(f'Aumentando 10%, temos {moedaspy.aumentar(preço, 10)}')
print(f'Diminuindo 13%, temos { moedaspy.diminuir(preço, 13)}')
