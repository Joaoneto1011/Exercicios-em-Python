#faça um programa que tenha uma funçao chamada area()
#que receba as dimensoes de um terreno retangular(largura e comprimento)
#e mostre a area do terreno

def area (largura, comprimento):
    Resultado_Area = largura * comprimento
    print(f'A largura é igual a {largura} e o comprimento é igual a {comprimento}')
    print(f'A area do terreno {largura}m x {comprimento}m é de {Resultado_Area:.2f}m²')

    print('-='*30)

print('     CONTROLE DE TERRENOS     ')
print('-'*30)
largura = float(input('Informe a largura do terreno (m): '))
comprimento = float(input('Informe o comprimento do terreno (m): '))
print('-='*30)

area(largura, comprimento)
