#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15 % de aumento

salario_funcionario = float(input('digite o salario do funcionario: '))

aumento = salario_funcionario * 0.15

novo_salario = salario_funcionario + aumento

print('O novo salario do funcionario com o aumento de 15% é de {} reais'.format(novo_salario))