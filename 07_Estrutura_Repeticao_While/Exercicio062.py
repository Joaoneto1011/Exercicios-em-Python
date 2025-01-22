#melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
#o programa encerra quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo),end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))

print('FIM')
