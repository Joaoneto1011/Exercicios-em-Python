#crie um programa que leia o nome e o preço de varios produtos.
#o programa devera perguntar se o usuario vai continuar. no final mostre: 
# A) qual é o total gasto na compra
# B) quantos produtos custam mais de 1000
# C) qual é o nome do produto mais barato

total_gasto = 0
produtos_acima_de_1000 = 0
produto_mais_barato = 0
produtos_comprados = 0
nome_produto_mais_barato = ''

while True:
    nome_produto = str(input('Digite o nome do produto: '))
    preço_produto = float(input('Digite o preço do produto: R$'))
    produtos_comprados += 1
    total_gasto += preço_produto
    
    if preço_produto > 1000:
        produtos_acima_de_1000 += 1
    
    if produtos_comprados == 1 or preço_produto < produto_mais_barato:
        produto_mais_barato = preço_produto
        nome_produto_mais_barato = nome_produto
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if resposta == 'N':
        break

    

print(f'O total gasto na compra é de R${total_gasto}reais')
print(f'Foram comprados {produtos_acima_de_1000} produtos custando acima de R$1000 reais')
print(f'{nome_produto_mais_barato} é o produto mais barato, custando R$ {produto_mais_barato} reais')