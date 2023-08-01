'''
Faça um programa que leia um angulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse triangulo
'''

import math

angulo = float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print(f"O angulo de {angulo} tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}")
