#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiusculas
#o nome com todas as letras minusculas
#quantas letras ao todo(sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele  tem {} letras'.format(dividido[0], len(dividido[0])))
