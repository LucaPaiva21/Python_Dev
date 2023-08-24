'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex:
5! = 5x4x3x2x1 = 120
'''

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(numero, 0, -1):
    fatorial *= i

print(f"{numero}! =", end=" ")

for i in range(numero, 0, -1):
    if i > 1:
        print(i, "x", end=" ")
    else:
        print(i, "=", fatorial)
