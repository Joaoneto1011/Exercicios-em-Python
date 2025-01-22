#crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços
# exemplo: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA

frase = str(input('Digite uma frase: ')).strip().upper() #strip serve para tirar os espaços da frase, e o upper para jogar tudo para maiusculo

palavras = frase.split() #isso serve pra pegar a frase digitada e esplitar ela em uma lista separada por palavras da frase

junto = ''.join(palavras) #isso serve para juntar a frase toda novamente, porem agora sem espaços entre as palavras, toda junta a frase

inverso = '' #criando uma variavel inverso para colocar a palavra toda juntada porem ao inverso

for letra in range(len(junto) -1, -1, -1): #isso serve para percorrer toda a string começando da ultima letra '-1', e indo ate a primeira letra '-1', voltando de uma em uma letra usando '-1'
    inverso = inverso + junto[letra] #o inverso agora vai receber cada letra da palavra juntada, uma por uma de tras pra frente, com o comando for encima
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto: # depois que o inverso receber cada letra da palavra juntada da variavel 'junto', se a palavra que for formada no inverso for a mesma que foi formada em junto, sera um palindromo
    print('Temos um palíndromo')

else:
    print('A frase digitada nao é um palíndromo')

    