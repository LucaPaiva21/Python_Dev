'''
Refaça o desafio 035 dos triangulos, acrescentando de mostrar que tipo de triangulo será formado

- Equeliatero: todos os lados iguais
- Isoceles: Dois lados iguais
- Escaleno: todos os lados diferentes
'''

lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if lado1 == lado2 == lado3:
    print("Seu triângulo é equilatero")
elif lado1 == lado2 != lado3 or lado2 == lado3 != lado1 or lado3 == lado1 != lado2:
    print("Seu triângulo é isoceles")
else:
    print("Seu triângulo é escaleno")
