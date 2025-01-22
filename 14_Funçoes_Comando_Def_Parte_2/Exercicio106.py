#faça um mini-sistema que utilize o interactive help do python
#o usuario vai digitar o comando e o manual vai aparecer.
#quando o usuario digitar a palavra 'FIM', o programa se encerrara
#OBS: use cores.

from time import sleep
c = ('\033[m',              # 0 - sem cores
         '\033[0;30;41m',   # 1 - vermelho
         '\033[0;30;42m',   # 2 - verde
         '\033[0;30;43m',   # 3 - amarelo
         '\033[0;30;44m',   # 4 - azul
         '\033[0;30;45m',   # 5 - roxo
         '\033[7;30m');      # 6 - branco


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(mensagem, cor = 0):
    tamanho = len(mensagem) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(f'   {mensagem}')
    print('~'* tamanho)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Funçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('VOLTE SEMPRE!', 1)
