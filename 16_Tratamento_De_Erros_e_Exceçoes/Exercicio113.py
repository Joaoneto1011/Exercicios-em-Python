#Reescreva a funçao leiaInt() que fizemos no desafio 104
#incluindo agora a possibilidade da digitaçao de um numero de tipo invalido.
#aproveite e crie tambem uma funçao leiaFloat() com a mesma funcionalidade.


def leiaInt(mensagem):
    """
    Le um numero inteiro do usuario, garantindo validaçao.
    :parametro mensagem: Mensagem exibida para o usuario.
    :return: Numero inteiro valido.
    """
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError: #use ValueError para tratar especificamente erro de conversao
            print('\033[0;31mERRO! Digite um numero inteiro valido. \033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuario. \033[m ')

def leiaFloat(mensagem):
    """
    Le um numero real (float) do usuario, garantindo validaçao.
    :parametro mensagem: Mensagem exibida para o usuario.
    :return: Numero real valido.
    """
    while True:
        try:
            n = float(input(mensagem))
            return n
        except ValueError: #use ValueError para tratar erro de conversao para float
            print('\033[0;31mERRO! Digite um numero real valido. \033[m')
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuario.  \033[m')

nInt = leiaInt('Digite um numero inteiro: ')
nFloat= leiaFloat('Digite um numero real: ')
print(f'O numero inteiro digitado foi {nInt} e o real foi {nFloat}')