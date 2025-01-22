def cifrar_palavra(palavra):
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvxz'
    palavra_cifrada = ''

    for letra in palavra:
        if letra in vogais:
            palavra_cifrada += letra
        else:
            # Encontra a vogal mais próxima
            if letra in 'bc':
                prox_vogal = 'a'
            elif letra in 'dfg':
                prox_vogal = 'e'
            elif letra in 'hjkl':
                prox_vogal = 'i'
            elif letra in 'mnpqr':
                prox_vogal = 'o'
            else:
                prox_vogal = 'u'

            # Encontra a próxima consoante
            index = consoantes.index(letra)
            prox_consoante = consoantes[index + 1] if index < len(consoantes) - 1 else letra

            # Constrói a palavra cifrada
            palavra_cifrada += letra + prox_vogal + prox_consoante

    return palavra_cifrada

# Leitura da palavra de entrada
palavra = input("Digite a palavra para cifrar: ")

# Chama a função de cifragem e imprime o resultado
print(cifrar_palavra(palavra))
