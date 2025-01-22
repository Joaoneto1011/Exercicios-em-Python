def moeda(valor = 0, simbolo = True):
    """
    Formata um numero como valor monetario.
    :parametro valor: O numero a ser formatado.
    :parametro simbolo: O simbolo da moeda (padrao: 'R$').
    :return: Uma string com o valor formatado como moeda.
    """
    valor_formatado = f'{valor:.2f}'.replace('.',',')
    return f'R${valor_formatado} ' if simbolo else valor_formatado

def aumentar(valor = 0, percentual = 0, simbolo = False):
    """Calcula o valor com o aumento percentual."""
    resultado =  valor + (valor * percentual / 100)
    return moeda(resultado) if simbolo else resultado

def diminuir(valor = 0, percentual = 0, simbolo = False):
    """Calcula o valor com a reduçao percentual."""
    resultado = valor - (valor * percentual / 100)
    return moeda(resultado) if simbolo else resultado

def dobro(valor = 0, simbolo = False):
    """Calcula o dobro do valor."""
    resultado = valor * 2
    return moeda(resultado) if simbolo else resultado

def metade(valor = 0, simbolo = False):
    """Calcula a metade do valor."""
    resultado = valor / 2
    return moeda(resultado) if simbolo else resultado

def resumo(valor = 0, aumento = 0, reduçao = 0):
    """
    Exibe um resumo com as operaçoes realizadas no valor.
    :parametro valor: O valor a ser analisado.
    :parametro aumento: Percentual de aumento a ser aplicado no valor.
    :parametro diminuir: Percentual de reduçao a ser aplicado no valor.
    :parametro simbolo: Se True, exibi os valores formatados como moeda.
    """
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor, True)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True )}')
    print(f'{reduçao}% de reduçao: \t{diminuir(valor, reduçao, True)}')
    print('-'*30)