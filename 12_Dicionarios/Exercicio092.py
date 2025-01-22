#crie um programa que leia nome, ano de nascimento e carteira de trabalho.
#e cadastre-os(com idade) em um dicionario.
#se por acaso o CTPS for diferente de ZERO, o dicionario recebera tambem o ano de contrataçao e o salario.
#alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
nome = str(input('NOME: '))
ano_nascimento = int(input('ANO DE NASCIMENTO: '))
carteira_de_trabalho = int(input('CARTEIRA DE TRABALHO (0 nao tem): '))
idade = datetime.now().year -  ano_nascimento   

dicionario = {'Nome': nome, 'Idade': idade, 'Carteira De Trabalho': carteira_de_trabalho}

if carteira_de_trabalho != 0:
    ano_contrataçao = int(input('ANO DE CONTRATAÇAO: '))
    salario = float(input('SALARIO: '))

    dicionario['Ano Contrataçao'] = ano_contrataçao
    dicionario['Salario'] = salario

    ano_aposentadoria = ano_contrataçao + 35
    idade_para_aposentar = (ano_contrataçao - ano_nascimento) + 35


    dicionario['Ano Aposentadoria'] = ano_aposentadoria
    dicionario['Idade Para Aposentar'] = idade_para_aposentar

print('-='* 30)
for k, v in dicionario.items():
    print(f'  - {k} tem o valor {v}')
print('-='* 30)
print(dicionario)