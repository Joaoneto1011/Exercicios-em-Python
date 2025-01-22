#desenvolva um programa que leia o primeiro termo e a razao de uma PA
#no final, mostre os 10 primeiros termos dessa progressao.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Informe a razao: '))

decimo_termo = primeiro_termo + (11 - 1) * razao

for c in range (primeiro_termo, decimo_termo, razao):
    print(c, end= ' -> ' )
print('acabou')