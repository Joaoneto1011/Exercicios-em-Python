#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m quadrados

largura = float(input('digite a largura da parede em metros: '))
altura = float(input('digite a altura da parede em metros: '))

area = largura * altura

print('A dimensao dessa parede tem {}x{} e uma area de {}'.format(largura,altura,area))

tinta = area / 2

print('Voce precisara usar {} litros de tinta'.format(tinta))