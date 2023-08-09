'''
Faça um programa que leia o coprimento do cateto
oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa
'''

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print(f"A hipotenusa vai medir: {hipotenusa}")