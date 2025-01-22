#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
#depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla.
import random

numeros = tuple(random.randint(1, 30) for _ in range(5))

print(f'Os numero sorteados da minha tupla sao: {numeros}')
print(f'O maior numero da tupla é o {max(numeros)}')
print(f'O menor numero da tupla é {min(numeros)}')

#1. random.randint(a, b)
#O que faz: Gera um único número inteiro aleatório entre a e b (inclusive).
#Quando usar:
#Quando precisa de um único número ou deseja criar uma lista de números manualmente.
#Não controla repetição automaticamente.
#Exemplo:
#import random
#num = random.randint(1, 10)  # Gera um número entre 1 e 10


#2. random.choices(population, k)
#O que faz: Retorna uma lista de tamanho k com elementos escolhidos da population (com repetição por padrão).
#Quando usar:
#Quando precisa de uma lista com valores que podem se repetir.
#Ideal para simulações ou cenários onde repetição é permitida.
#Exemplo:
#import random
#nums = random.choices(range(1, 11), k=5)  # Gera 5 números, podendo repetir



#3. random.sample(population, k)
#O que faz: Retorna uma lista de tamanho k com elementos únicos retirados da population (sem repetição).
#Quando usar:
#Quando precisa de números únicos ou quer criar uma lista sem duplicatas.
#Exemplo:
#import random
#nums = random.sample(range(1, 11), 5)  # Gera 5 números únicos



#4. random.uniform(a, b)
#O que faz: Gera um número aleatório de ponto flutuante entre a e b.
#Quando usar:
#Quando trabalha com números decimais ou precisa simular valores contínuos.
#Exemplo:
#import random
#num = random.uniform(1.5, 5.5)  # Gera um número entre 1.5 e 5.5



#5. random.random()
#O que faz: Retorna um número de ponto flutuante aleatório entre 0 e 1.
#Quando usar:
#Quando precisa de um valor probabilístico ou quer escalar números manualmente.
#Exemplo:
#import random
#num = random.random()  # Gera um número entre 0 e 1