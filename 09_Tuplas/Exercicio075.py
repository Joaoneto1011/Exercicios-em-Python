#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
# A) quantas vezes apareceu o valor 9
# B) em que posiçao foi digitado o primeiro valor 3
# C) quais foram os numeros pares

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))

tupla = (valor1, valor2, valor3, valor4)

print(f'Voce digitou os valores:  {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
  print(f'O valor 3 apareceu na {tupla.index (3)+1} posiçao')
else:
   print('O valor 3 nao foi digitado em nenhuma posiçao')
print('Os valores pares digitados foram ', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')