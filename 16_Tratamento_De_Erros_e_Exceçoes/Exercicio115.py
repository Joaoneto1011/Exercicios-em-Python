#crie um pequeno sistema modularizado.
#que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#o sistema so vai ter 2 opçoes:
#cadastrar uma nova pessoas e listar todas as pessoas cadastradas.

from biblioteca.interfaces import menu, cabeçalho
from time import sleep
from biblioteca.arquivo import arquivoExiste, criarArquivo, lerArquivo, cadastrarPessoa

# Nome do arquivo que será utilizado como base de dados
arq = 'cursoemvideo.txt'

# Verifica se o arquivo existe. Caso não exista, cria o arquivo.
if not arquivoExiste(arq):
    criarArquivo(arq)

# Loop principal do programa
while True:
    # Exibe o menu e captura a opção escolhida pelo usuário
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    
    if resposta == 1:
        # Opção 1: Ler e exibir as pessoas cadastradas no arquivo
        lerArquivo(arq)

    elif resposta == 2:
        # Opção 2: Realizar um novo cadastro
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))  # Solicita o nome da pessoa
        idade = int(input('Idade: '))  # Solicita a idade da pessoa
        cadastrarPessoa(arq, nome, idade)

    elif resposta == 3:
        # Opção 3: Sair do sistema
        cabeçalho('Saindo do sistema... até logo!')
        break  # Encerra o loop principal

    else:
        # Caso o usuário insira uma opção inválida
        print('\033[31mERRO! Digite uma opção válida! \033[m')
        sleep(2)

