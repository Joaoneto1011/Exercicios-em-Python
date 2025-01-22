#crie um programa que tenha uma tupla com varias palavras(nao usar acentos).
#depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
        print(f'\nNa palavra {p.upper()} temos as vogais ', end=' ')
        for letra in p:
                if letra.lower() in 'aeiou':
                    print(letra, end=' ')