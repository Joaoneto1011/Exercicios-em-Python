#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da prestaçao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado

valor_casa = float(input('Digite o valor da casa: '))
salario_comprador = float(input('Digite o salario do comprador da casa: '))
pagamento_em_anos = int(input('Digite em quantos anos o comprador vai pagar a casa:  '))

prestaçao_mensal = valor_casa / (pagamento_em_anos * 12)

if prestaçao_mensal > (salario_comprador * 0.30):
    print('A prestaçao mensal excedeu 30% do seu salario, o emprestimo foi negado')

else:
    print('O emprestimo foi aceito, voce tera uma prestaçao mensal de R$ {:.2f} reais'.format(prestaçao_mensal))