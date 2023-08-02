'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
# Importei a biblioteca math por conta do valor de pi
import math

# Valor do raio sendo recebido pelo usúario
raio = float(input("Digite o valor do raio: "))

# Usando o math.pi para que o valor seja expresso corretamente
area = math.pi * raio**2

# Resultado que será msotardo para o usuário
print(f"A area do círculo é: {area}")
