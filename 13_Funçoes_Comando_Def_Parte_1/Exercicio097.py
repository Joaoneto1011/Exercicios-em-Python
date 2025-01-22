#faça um programa que tenha uma funçao chamada escreva()
#que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel
#Ex: escreve('Ola, Mundo!')
#saida:(---------)
#      (ola mundo)
#      (---------)


def escreva(txt):
    repetiçoes = len(txt) + 4
    print('~' * repetiçoes)
    print(f'  {txt}')
    print('~' * repetiçoes)

escreva('Gustavo Guanabara')
escreva('Curso de python no Youtube')
escreva('CeV')