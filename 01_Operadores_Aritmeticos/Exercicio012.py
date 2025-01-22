#faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto.

preço_produto = float(input('informe o preço do produto: '))

desconto_produto = preço_produto * 0.05

novo_preço = preço_produto - desconto_produto

print('O novo preço do produto com o desconto de 5%  é de {} reais'.format(novo_preço))

