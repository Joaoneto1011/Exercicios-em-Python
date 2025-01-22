#crie um programa que leia duas notas de um aluno e calcule a media, mostrando uma mensagem no final, de acordo com a media atingida:
#media abaixo de 5.0: reprovado
#media entre 5.0 e 6.9: recuperaçao
#media 7.0 ou superior: aprovado

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Voce foi reprovado, sua media foi {} e ficou abaixo de 5.0'.format(media))

elif media >= 5.0 and media <= 6.9:
    print('Voce ficou de recuperaçao, sua media foi {} e ficou abaixo de 7.0 '.format(media))

else:
    print('Voce foi aprovado, sua media foi {} e ficou acima de 6.9'.format(media))