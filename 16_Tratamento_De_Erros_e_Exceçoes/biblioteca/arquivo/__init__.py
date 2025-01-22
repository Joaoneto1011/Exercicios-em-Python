from biblioteca.interfaces import cabeçalho

def arquivoExiste(nome):
    """
    Verifica se o arquivo especificado existe no diretório atual.
    
    Parâmetros:
    nome (str): Nome do arquivo a ser verificado.
    
    Retorno:
    bool: Retorna True se o arquivo existir, caso contrário False.
    """
    try:
        a = open(nome, 'rt')  # Tenta abrir o arquivo no modo leitura (texto).
        a.close()
    except FileNotFoundError:  # Captura a exceção se o arquivo não existir.
        return False
    else:
        return True


def criarArquivo(nome):
    """
    Cria um novo arquivo com o nome especificado caso ele não exista.
    
    Parâmetros:
    nome (str): Nome do arquivo a ser criado.
    
    Retorno:
    None
    """
    try:
        a = open(nome, 'wt+')  # Cria um arquivo no modo de escrita (texto).
        a.close()
    except Exception:  # Captura qualquer exceção que ocorra ao criar o arquivo.
        print('Erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')  # Confirmação de sucesso.


def lerArquivo(nome):
    """
    Lê o conteúdo do arquivo especificado e exibe os dados formatados no console.
    
    Parâmetros:
    nome (str): Nome do arquivo a ser lido.
    
    Retorno:
    None
    """
    try:
        a = open(nome, 'rt')  # Abre o arquivo no modo leitura (texto).
    except Exception:  # Captura qualquer erro ao abrir o arquivo.
        print('ERRO na criação do arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')  # Exibe o cabeçalho com o título.
        for linha in a:
            dado = linha.split(';')  # Divide cada linha em nome e idade.
            dado[1] = dado[1].replace('\n', '')  # Remove a quebra de linha.
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # Exibe os dados formatados.
    finally:
        a.close()  # Garante que o arquivo será fechado ao final.


def cadastrarPessoa(arq, nome='desconhecido', idade=0):
    """
    Cadastra uma nova pessoa no arquivo, registrando o nome e a idade.
    
    Parâmetros:
    arq (str): Nome do arquivo onde os dados serão registrados.
    nome (str): Nome da pessoa (padrão: 'desconhecido').
    idade (int): Idade da pessoa (padrão: 0).
    
    Retorno:
    None
    """
    try:
        a = open(arq, 'at')  # Abre o arquivo no modo de anexação (adicionar texto).
    except Exception:  # Captura qualquer erro ao abrir o arquivo.
        print(f'Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')  # Escreve os dados no arquivo no formato nome;idade.
        except Exception:  # Captura erros ao tentar escrever no arquivo.
            print(f'ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')  # Confirmação de sucesso.
        finally:
            a.close()  # Garante que o arquivo será fechado.

