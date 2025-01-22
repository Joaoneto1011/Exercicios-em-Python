#faça um programa que tenha uma funçao chamada notas()
#que pode receber varias notas de alunos e vai retornar um dicionario
#com as seguintes informaçoes:
#quantidade de notas, a maior nota, a menor nota, a media da turma e a situaçao(opcional)
#adicione tambem as docstrings da funçao.

quantidade_alunos = 0
quantidade_notas = 0
maior_nota = 0
menor_nota = 9999
soma_notas = 0
while True:
    print('-='* 20)
    notas_alunos = float(input(f'Informe a nota do {quantidade_alunos + 1} aluno: '))
    quantidade_notas += 1
    quantidade_alunos += 1
    soma_notas += notas_alunos

    if notas_alunos > maior_nota:
        maior_nota = notas_alunos

    if notas_alunos < menor_nota:
        menor_nota = notas_alunos

    media_turma = soma_notas / quantidade_notas

    if media_turma >= 7.0:
        situaçao = 'BOA'

    elif media_turma >= 5.0 and media_turma < 7.0:
        situaçao = 'REGULAR'

    else:
        situaçao = 'PESSIMA'


    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if continuar == 'N':
        break

dicionario = {'Quantidade de Notas': quantidade_notas, 'Maior Nota':maior_nota, 'Menor Nota': menor_nota, 'Media Turma': media_turma, 'Situaçao': situaçao }

print('-='*20)
print(dicionario)
