#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra 'A'
#em que posiçao ela aparece a primeira vez
#em que posiçao ela aparece a ultima vez

frase = str(input('Digite uma frase qualquer: ')).upper().strip()

print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(frase.find('A')+ 1))
print('A ultima letra A apareceu na posiçao {}'.format(frase.rfind('A')+ 1))
