#faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
#o programa sera interrompido quando o numero solicitado for negativo

numero = 0

while True:
    numero = int(input('Digite um numero para consultar sua tabuada: '))
    if numero < 0:
        break
    for c in range(1, 11):
     print(f'{numero} X {c} = {numero * c}')

print('Tabuada encerrada')