#crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
#seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta.

expressao = input("Digite uma expressão: ")
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')  # Adiciona à pilha quando encontra '('
    elif simbolo == ')':
        if pilha:  # Se houver algo na pilha, remove o último '('
            pilha.pop()
        else:  # Se não houver, significa que a expressão está inválida
            pilha.append(')')  # Marca o erro
            break

# Verifica se a pilha está vazia
if not pilha:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")

