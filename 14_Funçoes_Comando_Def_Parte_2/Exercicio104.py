#crie um programa que tenha uma funçao chamada leiaInt()
#que vai funcionar de forma semelhante a funçao input() do python.
#so que fazendo a validaçao para aceitar apenas valor numerico.
#EX: n = leiaInt('Digite um n')


def leiaInt(mensagem):
    ok = False
    valor = 0

    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        
        if ok:
            break

    return valor
n = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {n}')