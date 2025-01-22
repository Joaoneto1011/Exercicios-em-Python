#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#exemplo: Ana maria de Souza
#primeiro = Ana
#segundo = Souza

nome = str(input('Digite seu nome completo: ')).strip()

nome_dividido = nome.split()

print('Seu primeiro nome é {}'.format(nome_dividido[0]))
print('Seu ultimo nome é {}'.format(nome_dividido[-1]))
