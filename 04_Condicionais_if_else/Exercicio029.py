#escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$ 7,00 por cada km acima do limite

velocidade_carro = float(input('Velocidade do carro: '))

if velocidade_carro > 80:
    print('Voce foi multado, a velocidade maxima permitida é de 80km/h')
    multa = (velocidade_carro - 80) * 7
    print('a multa recebida vai custar R$ {} reais '.format(multa))

print('tenha um bom dia! dirija com segurança ')



