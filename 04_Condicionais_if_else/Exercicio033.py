#faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.

Num1 = int(input('Digite o primeiro numero: '))
Num2 = int(input('Digite o segundo numero: '))
Num3 = int(input('Digite o terceiro numero: '))

# verificando o menor numero
menor = Num1

if Num2 < Num1 and Num2 < Num3:
    menor = Num2

if Num3 < Num1 and Num3 < Num2:
    menor = Num3

# verificando o maior numero
maior = Num2

if Num1 > Num2 and Num1 > Num3:
    maior = Num1

if Num3 > Num2 and Num3 > Num1:
    maior = Num3

print('o menor valor digitado é {}'.format(menor))
print('o maior valor digitado é {}'.format(maior))
