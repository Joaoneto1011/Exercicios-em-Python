#desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25: peso ideal
#entre 25 e 30: sobrepeso
#entre 30 e 40: obesidade
#acima de 40: obesidade morbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print('O seu IMC ficou em {:.1f}, voce esta abaixo do peso'.format(IMC))

elif IMC >= 18.5 and IMC < 25:
    print('O seu IMC ficou em {:.1f}, voce esta no peso ideal'.format(IMC))

elif IMC >= 25 and IMC < 30:
    print('O seu IMC ficou em {:.1f}, voce esta com sobrepeso'.format(IMC))

elif IMC >= 30 and IMC < 40:
    print('O seu IMC ficou em {:.1f}, voce esta com obesidade'.format(IMC))

elif IMC > 40:
    print('O seu IMC ficou em {:.1f}, voce esta com obesidade morbida'.format(IMC))