#faça um programa que leia um numero qualquer e mostre seu fatorial
#exemplo: 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um numero para calcular seu fatorial: '))

c = numero
f = 1
print('Calculando {}! = '.format(numero), end= '')

while c > 0:
    print('{}'.format(c), end='') #enquanto c for maior que 0, escreve c na tela, sendo que c é igual ao numero digitado
    print(' x ' if c > 1 else ' = ', end= '')# coloque X na frente se c for maior que 1, senao coloque = na frente
    f = f * c #f começa em 1, para calcular o fatorial que vai ser F vezes C que é o numero digitado
    c = c - 1 # a cada multiplicaçao feita, decrementa - 1 ao C, enquanto o C for maior que 0, após isso termina a multiplicaçao

print('{}'.format(f))