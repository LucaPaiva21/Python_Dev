'''
Faça um Programa que leia três números e mostre o maior deles.
'''
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior = 0

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print("="*40)
print("Os números informados foram:")
print(f"Número 1: {n1}\nNúmero 2: {n2}\nNúmero 3: {n3}\nO maior dos três foi: {maior}")
print("="*40)
