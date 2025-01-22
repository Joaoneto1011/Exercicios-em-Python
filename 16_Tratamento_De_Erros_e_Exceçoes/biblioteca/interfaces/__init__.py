def leiaInt(mensagem):
    """
    Lê um número inteiro do usuário, garantindo que a entrada seja válida.
    
    Parâmetros:
    mensagem (str): Mensagem exibida ao usuário solicitando o número.
    
    Retorno:
    int: Número inteiro fornecido pelo usuário.
    """
    while True:
        try:
            n = int(input(mensagem))  # Tenta converter a entrada do usuário em um número inteiro.
            return n  # Retorna o número inteiro se a conversão for bem-sucedida.
        except ValueError:  # Trata especificamente o erro de conversão para inteiro.
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
        except KeyboardInterrupt:  # Trata a interrupção pelo teclado (CTRL+C).
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário. \033[m')
            return 0  # Retorna 0 como valor padrão quando o usuário interrompe.


def linha(tamanho=42):
    """
    Gera uma linha horizontal composta por caracteres '-' para formatar a interface.
    
    Parâmetros:
    tamanho (int): Comprimento da linha (padrão: 42).
    
    Retorno:
    str: Uma string composta por '-' no comprimento especificado.
    """
    return '-' * tamanho  # Retorna uma string com o número de '-' especificado.


def cabeçalho(texto):
    """
    Exibe um cabeçalho formatado com texto centralizado, delimitado por linhas horizontais.
    
    Parâmetros:
    texto (str): Texto a ser exibido no cabeçalho.
    
    Retorno:
    None
    """
    print(linha())  # Imprime a linha superior.
    print(texto.center(42))  # Imprime o texto centralizado em 42 caracteres.
    print(linha())  # Imprime a linha inferior.


def menu(lista):
    """
    Exibe um menu numerado com as opções fornecidas e solicita uma escolha válida do usuário.
    
    Parâmetros:
    lista (list): Lista de strings representando as opções do menu.
    
    Retorno:
    int: Número inteiro correspondente à opção escolhida pelo usuário.
    """
    cabeçalho('MENU PRINCIPAL')  # Exibe o título do menu.
    c = 1  # Contador para numerar as opções.
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')  # Exibe as opções formatadas com cores.
        c += 1
    print(linha())  # Imprime uma linha horizontal após as opções.
    opcao = leiaInt('\033[32mSua Opção: \033[m')  # Solicita uma opção válida do usuário.
    return opcao  # Retorna a opção escolhida.
