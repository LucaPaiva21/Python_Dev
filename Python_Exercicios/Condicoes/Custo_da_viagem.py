'''
Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando 0,50 reais por km para viagem ate 200km,
e 0,45 reais para viagens mais longas
'''
distancia_viagem = float(input("Informe a distância da viagem para calcularmos o preço: "))

if distancia_viagem > 200:
    valor1 = distancia_viagem * 0.45
    print(f"O valor da sua viagem é: {valor1} reais. Sua viagem é um pouquinho longa")
else:
    valor2 = distancia_viagem * 0.50
    print(f"O valor da sua viagem é: {valor2} reais. Sua viagem até que é curtinha.")
