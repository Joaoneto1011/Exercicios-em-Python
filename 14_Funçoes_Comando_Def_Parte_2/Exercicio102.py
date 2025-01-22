#crie um programa que tenha uma funçao fatorial() que receba dois parametros:
#o primeiro que indique o numero a calcular.
#e o outro chamado show, que sera um valor logico(opcional)
#indicando se sera mostrado ou nao na tela o processo de calculo do fatorial.


def fatorial(num, show = False):

    """
    -> Calcula o fatorial de um numero;
    Parametro n: O numero a ser calculado.
    Parametro show: (opcional) Mostrar ou nao a conta.
    Return: O valor do fatorial de um numero n.
    """
    contador = num
    fatorial = 1
    while contador > 0:
        if show == True:
            print(f'{contador}', end='')
            print(f' X ' if contador > 1 else ' = ', end='')
            fatorial = fatorial * contador
            contador = contador - 1
        else:
            fatorial = fatorial * contador
            contador = contador - 1

    return fatorial


print(fatorial(5, show=True))