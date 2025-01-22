#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a R$1250.00, calcule um aumento de 10%.
#para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salario? '))

if salario <= 1250.00:
    aumento = salario * 0.15
    print('Seu salario que era de R$ {} reais, agora voce recebera um aumento de R$ {} reais e seu salario sera R$ {} reais'.format(salario, aumento, (salario + aumento)))

else:
    aumento = salario * 0.10
    print('Seu salario que era de R$ {} reais, agora voce recebera um aumento de R$ {} reais e seu salario sera R$ {} reais'.format(salario, aumento, (salario + aumento)))
