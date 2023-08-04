'''
Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.

ex:
Digite um número: 1834

unidade = 4
dezena = 3
centena = 8
milhar = 1
'''

numero = int(input("Digite um número inteiro qualquer: "))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f"Unidade é: {unidade}")
print(f"Dezena é: {dezena}")
print(f"Centena é: {centena}")
print(f"Milhar é: {milhar}")

