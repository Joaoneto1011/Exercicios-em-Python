#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math
angulo = float(input('Digite o valor de um angulo: '))

valor_seno = math.sin(math.radians(angulo))
valor_cosseno = math.cos(math.radians(angulo))
valor_tangente = math.tan(math.radians(angulo))

print('O valor do seno do angulo {} é igual a {:.2f}'.format(angulo,valor_seno ))
print('O valor do cosseno do angulo {} é igual a {:.2f}'.format(angulo, valor_cosseno))
print('O valor da tangente do angulo {} é igual a {:.2f} '.format(angulo, valor_tangente))