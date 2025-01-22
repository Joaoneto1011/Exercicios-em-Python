#crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
#no final, mostre um boletim contendo a media de cada um
#e permita que o usuario possa mostras as notas de cada aluno individualmente.

lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    
    continuar = str(input('Voce quer continuar? [S/N]')).strip().upper()

    if continuar == 'N':
        break

    while continuar not in 'SN':
        continuar = str(input('Voce quer continuar? [S/N]'))

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 26)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4} {aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opçao = int(input('Mostrar notas de qual aluno?(999 interrompe)'))
    if opçao == 999:
        print('FINALIZANDO...')
        break
    if opçao <= len(lista) - 1:
        print(f'Notas de {lista[opçao][0]} sao {lista[opçao][1]}')
    