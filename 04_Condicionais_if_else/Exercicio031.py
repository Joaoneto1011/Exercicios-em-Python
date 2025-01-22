#desenvolva um programa que pergunta a distancia de uma viagem em km.
#calcule o preço da passagem, cobrando R$0.50 por km para viagens de ate 200km
# e cobre R$0.45 para viagens acima de 200 km

distancia_em_km = float(input('Digite a distancia percorrida em KM: '))
print('a distancia a ser percorrida na sua viagem é de {} KM '.format(distancia_em_km))
if distancia_em_km <= 200:
    preço_passagem = distancia_em_km * 0.50

else:
    preço_passagem = distancia_em_km * 0.45

print('o preço a ser pago da passagem é de R$ {} reais'.format(preço_passagem))
print('tenha uma boa viagem')