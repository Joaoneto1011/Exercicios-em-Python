#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#exemplo: digite um numero: 1834
#unidade: 4, dezena: 3, centena: 8, milhar: 1

numero = int(input('Digite um numero de 0 a 9999: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print('A unidade do numero {} é igual a {}'.format(numero, unidade))
print('A dezena do numero {} é igual a {}'.format(numero, dezena))
print('A centena do numero {} é igual a {}'.format(numero, centena))
print('O milhar do numero {} é igual a {}'.format(numero, milhar))