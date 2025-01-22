#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = float(input('digite o valor em metros:'))

km = metros * 0.0010

hm = metros * 0.010

dam = metros * 0.10

decametros = metros * 10

centimetros = metros * 100

milimetros = metros * 1000
print('A medida de {} metros equivale a {} km e a {} hm'.format(metros, km, hm))
print('A medida de {} metros equivale a {} dam e a {} decametros'.format(metros, dam, decametros))
print('A medida de {} metros equivale a {} centimetros e a {} milimetros'.format(metros,centimetros,milimetros))
