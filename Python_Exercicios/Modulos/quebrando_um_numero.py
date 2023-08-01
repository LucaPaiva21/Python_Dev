'''
Crie um programa que leia um número real quealquer
e mostre na tela sua porção inteira

ex:.
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
'''
import math

num = float(input("Digite um número real: "))

print(f"O número {num} tem a parte inteira {math.trunc(num)}")