'''
Crie um programa que leia quanto dinheiro um pessoa tem na carteira
e mostre quantos dólares ela pode comprar
considere us$= r$=5,00
'''
reais = int(input("Digite quanto você tem em reais: "))

dolar = reais / 5.00

print(f"Com R${reais} você pode comprar US${dolar}")