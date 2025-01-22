galera = []
dado = []
totalmaior = totalmenor = 0

for contador in range(0, 3):
    dado.append(str(input('NOME: ')))
    dado.append(int(input('IDADE: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >=21:
        print(f'{pessoa[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totalmenor += 1

print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')