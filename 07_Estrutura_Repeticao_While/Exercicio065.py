#crie um programa que leia varios numeros inteiros pelo teclado.
#no final da execuçao, mostre a media entre todos os valores e qual foi o maior e o menor valor lido.
#o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.

resposta = 'S'
valores_digitados = 0
soma = 0

while resposta in 'Ss':
    numero = int(input('Digite um numero: '))
    valores_digitados =  valores_digitados + 1
    soma = soma + numero
    if valores_digitados == 1:
        maior_valor = numero
        menor_valor = numero
    else:
        if numero > maior_valor:
            maior_valor = numero
        if numero < menor_valor:
            menor_valor = numero
    
    resposta = str(input('Voce quer continuar? [S/N]: ')).upper().strip()[0]

    while resposta not in 'SN':
        resposta = str(input('Voce quer continuar? [S/N]: ')).upper().strip()



media = soma / valores_digitados
print('Voce digitou {} numeros, a soma entre eles é de {} e a media é {}'.format(valores_digitados, soma, media))
print('O maior valor é {} e o menor valor é {}'.format(maior_valor, menor_valor))
print('ACABOU')