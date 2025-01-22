#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo premitivo e todas as informaçoes possivies sobre ela

n =(input('digite algo: '))

print('O tipo premitivo desse valor é', type(n))
print('So tem espaços?', n.isspace())
print('É um numero?', n.isnumeric())
print('É alfabetico?', n.isalpha())
print('É alfanumerico?', n.isalnum())
print('Esta em maiusculas?', n.isupper())
print('Esta em minusculas?', n.islower())
print('Esta capitalizada?', n.istitle())
