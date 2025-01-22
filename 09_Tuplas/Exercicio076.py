#crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
#no final, mostre uma listagem de preços, organizando os dados em forma tabular

produtos = ('Mouse', 20.0, 'Notebook', 3000.00, 'Carregador', 200.50, 'Fone', 50.99)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*50)
for posiçao in range (0, len(produtos)):
    if posiçao % 2 == 0:
        print(f'{produtos[posiçao]:.<30}', end='')

    else:
        print(f'R${produtos[posiçao]:.>7.2f}')
print('-'*50)