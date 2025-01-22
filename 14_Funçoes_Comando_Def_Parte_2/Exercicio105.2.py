#faça um programa que tenha uma funçao chamada notas()
#que pode receber varias notas de alunos e vai retornar um dicionario
#com as seguintes informaçoes:
#quantidade de notas, a maior nota, a menor nota, a media da turma e a situaçao(opcional)
#adicione tambem as docstrings da funçao.


def notas(* num, sit = False):

    """
    -> Funçao para analisar notas e situaçoes de varios alunos.
    Parametro n: uma ou mais notas dos alunos (aceita varias)
    Parametro sit: valor opcional, indicando se deve ou nao adicionar a situaçao
    Return: dicionario com varias informaçoes sobre a situaçao da turma.
    """

    dicionario = {}
    dicionario['Total de Notas'] = len(num)
    dicionario['Maior Nota'] = max(num)
    dicionario['Menor Nota'] = min(num)
    dicionario['Media Turma'] = sum(num) / len(num)

    if sit:
        if dicionario['Media Turma'] >= 7.0:
            dicionario['Situaçao'] = 'BOA'

        elif dicionario['Media Turma']>= 5.0:
            dicionario['Situaçao'] = 'REGULAR'

        else:
            dicionario['Situaçao'] = 'RUIM'

    print(f'Recebi as notas {num}')
    print('-='*20)

    return dicionario


resposta = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resposta)
