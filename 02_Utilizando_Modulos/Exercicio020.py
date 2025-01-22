#o mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')

nomes = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(nomes)

print('A ordem escolhida dos nomes será', nomes)