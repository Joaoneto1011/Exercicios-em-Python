#crie um programa que leia dois valores e mostre um menu na tela:
# 1 para somar
# 2 para multiplicar
# 3 para mostrar o maior numero
# 4 para digitar novos numeros
# 5 para sair do programa
# seu programa devera realizar a operaçao solicitada em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [1] Para somar os dois valores
    [2] Para multiplicar os dois valores
    [3] Para mostrar o maior valor
    [4] Para digitar novos numeros
    [5] Para sair do programa''')
    opçao = int(input('Digite sua opçao: '))

    if opçao == 1:
        soma = valor1 + valor2
        print('A soma entre  {} + {} é = a {} '.format(valor1, valor2, soma))

    elif opçao == 2:
        multiplicaçao = valor1 * valor2
        print('A multiplicaçao entre  {} X {} é = a {}'.format(valor1, valor2, multiplicaçao))

    elif opçao == 3:
        if valor1 > valor2:
            maior_valor = valor1
        elif valor2 > valor1:
            maior_valor = valor2
            print('O maior valor entre {} e {} é o {}'.format(valor1, valor2, maior_valor))
        else:
            valor1 == valor2
            print('Os numeros {} e {} sao iguais'.format(valor1, valor2))

    elif opçao == 4:
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite um novo valor: '))
        print('Os novos valores digitados sao {} e {}'.format(valor1, valor2))

    elif opçao == 5:
        print('Saindo do programa...')

    else:
        print('Opçao invalida. tente novamente')
print('FIM, volte sempre!')