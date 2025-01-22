#refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
#equilatero: todos os lados iguais
#isosceles: dois lados iguais
#escaleno: todos os lados diferentes

reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('Essas retas podem formar um triangulo')

    if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print('Essas retas {}, {}, {} formam um triangulo equilatero, pois todos os lado sao iguais'.format(reta1, reta2, reta3))
    elif (reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3):
        print('Essas retas {},{},{} formam um triangulo isosceles, pois tem dois lados iguais'.format(reta1, reta2, reta3))
        
    elif  (reta1 != reta2) and (reta1 != reta3) and (reta2 != reta3):
        print('Essas retas {},{},{} formam um triangulo escaleno, pois todos os lados sao diferentes'.format(reta1, reta2, reta3))

else:
    print('Essas retas nao podem formar um triangulo')