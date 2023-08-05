'''
Faça um programa que leia três números e mostre
qual é o maior e qual o menor.
'''

numero = int(input("Digite um número: "))
numero2 = int(input("Digite um segundo número: "))
numero3 = int(input("Digite um terceiro número: "))

maior = 0

if numero > maior:
    maior = numero
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

print(f"Os números informados foram: {numero}, {numero2}, {numero3}.")
print(f"O maior entre eles foi: {maior}")