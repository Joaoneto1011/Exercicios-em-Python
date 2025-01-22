#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media

nota1 = float(input('digite a primeira nota do aluno: '))
nota2 = float(input('digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print('A media entre {} e {} é igual a {:.1f}'.format(nota1,nota2,media))