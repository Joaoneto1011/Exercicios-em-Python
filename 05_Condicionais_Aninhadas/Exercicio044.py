#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento:
#a vista dinheiro/cheque: 10% de desconto
#a vista no cartao: 5% de desconto
#em ate 2 vezes no cartao: preço normal
#3 vezes ou mais no cartao: 20% de juros

preço_produto= float(input('Digite o preço do produto a ser pago: '))

print('''FORMAS DE PAGAMENTO: 
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA NO CARTAO
[3] EM ATE 2 VEZES NO CARTAO
[4] 3 VEZES OU MAIS NO CARTAO''')

opçao = int(input('Escolha uma das opçoes: '))

if opçao == 1:
    preço_com_desconto = preço_produto - (preço_produto * 0.10)
    print('O produto que custa R$ {} reais, agora com o desconto de 10% custara R$ {} reais '.format(preço_produto, preço_com_desconto))

elif opçao == 2:
    preço_com_desconto = preço_produto - (preço_produto * 0.05)
    print('O produto que custava R$ {} reais, agora com o desconto de 5% custara R$ {} reais'.format(preço_produto, preço_com_desconto))

elif opçao == 3:
    print('O preço do produto continuara no mesmo valor de R$ {} reais'.format(preço_produto))

elif opçao == 4:
    preço_com_juros = preço_produto + (preço_produto * 0.2)
    print('O preço do produto que custa R$ {} reais, agora com o juros de 20% custara R$ {} reais'.format(preço_produto, preço_com_juros))

else:
    print('Essa opçao é invalida, escolha uma opçao valida e tente novamente!')