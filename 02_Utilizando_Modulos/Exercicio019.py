#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

Primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
Segundo_aluno = str(input('Digite o nome do segundo aluno: '))
Terceiro_aluno = str(input('Digite o nome do terceiro aluno: '))
Quarto_aluno = str(input('Digite o nome do quarto aluno: '))

nomes = [Primeiro_aluno, Segundo_aluno, Terceiro_aluno, Quarto_aluno]

nome_escolhido = random.choice(nomes)

print('O aluno sorteado e escolhido foi {}'.format(nome_escolhido))
