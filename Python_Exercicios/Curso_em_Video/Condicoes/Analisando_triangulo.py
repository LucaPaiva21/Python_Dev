'''
Desenvolva um programa que leia o comprimento de tres retas e diga ao usúario
se elas podem ou não formar um triângulo
'''
a = float(input("DIgite o comprimento da reta: "))
b = float(input("DIgite o comprimento da reta: "))
c = float(input("DIgite o comprimento da reta: "))

if a + b > c and a + c > b and b + c > a:
    print("As retas podem formar um triângulo")
else:
    print("As retas não podem formar um triângulo")
