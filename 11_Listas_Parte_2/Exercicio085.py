#crie um programa onde o usuario possa digitar sete valores numericos
#e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
#no final, mostre os valores pares e impares em ordem crescente.

dados = [[],[]]
for c in range(1, 8):
    numero = int(input(f'Digite o {c} valor: '))

    if numero % 2 == 0:
        dados[0].append(numero)
    else:
        dados[1].append(numero)

dados[0].sort()
dados[1].sort()
print(f'Os valores pares digitados foram {dados[0]}')
print(f'Os valores impares digitados foram {dados[1]}')