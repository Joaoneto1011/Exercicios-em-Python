#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# calcule o preço a pagar,sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado

km_percorridos = float(input('digite a quantidade de km percorridos: '))

dias_alugados = int(input('digite a quantidade de dias o carro foi alugado: '))

preço_a_pagar = (dias_alugados * 60) + (km_percorridos * 0.15)

print('O preço a pagar pelo carro é de R${}'.format(preço_a_pagar))