'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = 0
menor = 0

# Maior
if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

# Menor
if n1 > menor:
    menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

# print maior e menor
print("="*40)
print("Os números informados foram:")
print(f"Número 1: {n1}\nNúmero 2: {n2}\nNúmero 3: {n3}\nO maior é: {maior}\nO menor é: {menor}")
print("="*40)