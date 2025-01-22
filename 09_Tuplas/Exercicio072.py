#crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte
#seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.

Tupla = ('zero ', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('digite um numero entre 0 e 20: '))

    while numero not in range (0, 21):
        numero = int(input('Tente novamente um numero entre 0 e 20: '))

    if numero == 15:
        print(Tupla[numero])
        break

    print(f'Voce digitou o numero {Tupla[numero]}')