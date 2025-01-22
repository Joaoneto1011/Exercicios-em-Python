#faça um programa que leia nome e media de um aluno.
#guardando tambem a situaçao em um dicionario.
#no final, mostre o conteudo da estrutura na tela.

aluno = {}

aluno['Nome'] = str(input('NOME: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situaçao'] = 'Aprovado'
elif aluno['Média'] >= 5 and aluno['Média'] < 7:
    aluno['Situaçao'] = 'Recuperaçao'
else:
    aluno['Situaçao'] = 'Reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f' -   {k} é {v}')
print(aluno)
