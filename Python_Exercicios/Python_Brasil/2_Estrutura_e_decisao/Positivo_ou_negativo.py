'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

# Número informado
numero = int(input("Digite um número positivo ou negativo: "))

# Metodo de decisão para saber o valor
if numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número {numero} é positivo.")