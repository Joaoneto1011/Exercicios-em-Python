#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere 1 dolar = 3,27 reais

dinheiro_na_carteira =  float(input('informe quanto de dinheiro voce tem na carteira: R$ '))

dolar = dinheiro_na_carteira / 3.27

print('Com R${:.2f} reais voce pode comprar US${:.2f} dolares'.format(dinheiro_na_carteira, dolar))