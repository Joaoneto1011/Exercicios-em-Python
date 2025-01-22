#crie um programa que vai ler varios numeros e colocar em uma lista.
#depois disso, crie duas listas extras que vao conter apenas valores pares e os valores impares digitados, respectivamente.
#ao final, mostre o conteudo das tres listas geradas.

lista_geral = []
lista_par = []
lista_impar = []
while True:
     numero = int(input('Digite qualquer numero: '))
     lista_geral.append(numero)

     if numero % 2 == 0:
          lista_par.append(numero)

     else:
           lista_impar.append(numero)
     
     continuar = str(input('Voce quer continuar? [S/N]: ')).upper().strip()

     if continuar == 'N':
          break
     
     while continuar not in 'SN':
          continuar = str(input('Voce quer continuar? [S/N]: ')).upper().strip()

lista_geral.sort()
lista_par.sort()
lista_impar.sort()
     
print(f'A lista completa é {lista_geral} ')
print(f'A lista de numeros pares é {lista_par} ')
print(f'A lista de numeros impares é {lista_impar}')