def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(F'Resultado da soma é igual a {s}')
    print('-='*30)
soma(4,5)
soma(8,9)
soma(2,1)



def contador (* num):
    tamanho = len(num)
    print('-='*30)
    print(f'Recebi os valores {num} e sao ao todo {tamanho} numeros ')
    print('-='*30)

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)



def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
valores = [2,4,6,8,10]
dobra(valores)
print(valores)



def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 3, 5)