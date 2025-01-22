#refaça o desafio 051, lendo o primeiro termo e a razao de uma PA
#mostrando os 10 primeiros termos da progressao usando a estrutura while

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Informe a razao: '))

termo = primeiro_termo
contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    contador = contador + 1

print('FIM')
