#escreve um programa que converta uma temperatura digitada em graus C e converta para F

temperatura_celsius = float(input('digite a temperatura em celsius: '))

fahrenheit = (temperatura_celsius * 9/5) + 32

print('{} graus celsius é igual a {} graus fahrenheit'.format(temperatura_celsius, fahrenheit))