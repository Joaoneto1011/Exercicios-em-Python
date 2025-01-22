#faça um programa que leia o sexo de uma pessoa, mas so aceite os valores digitados 'M' ou 'F'.
#caso esteja errado, peça a digitaçao novamente ate ter um valor correto.

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()

while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()

print('Sexo {} registrado com sucesso'.format(sexo))