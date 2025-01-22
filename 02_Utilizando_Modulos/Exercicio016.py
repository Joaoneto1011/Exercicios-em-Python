#crie um programa que leia um numero real qualquer e mostre na tela a sua porçao inteira

from math import trunc
numero = float(input('Digite um numero real qualquer: '))
porçao_inteira = trunc(numero)
print('A porçao inteira do numero {} é igual a {}'.format(numero, porçao_inteira))