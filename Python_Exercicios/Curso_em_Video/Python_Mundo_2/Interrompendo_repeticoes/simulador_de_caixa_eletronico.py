'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado (numero inteiro) e o
programa vai informar quantas cedulas de cada valor serao entregues

obs: considere que o caixa possui cedulas de 50, 20, 10 e de 1
'''
valor_saque = int(input("Digite o valor a ser sacado: "))

cedula_50 = 0
cedula_20 = 0
cedula_10 = 0
cedula_1 = 0

while valor_saque >= 50:
    cedula_50 += 1
    valor_saque -= 50

while valor_saque >= 20:
    cedula_20 += 1
    valor_saque -= 20

while valor_saque >= 10:
    cedula_10 += 1
    valor_saque -= 10

while valor_saque >= 1:
    cedula_1 += 1
    valor_saque -= 1

print(f"Quantidade de cédulas de R$50: {cedula_50}")
print(f"Quantidade de cédulas de R$20: {cedula_20}")
print(f"Quantidade de cédulas de R$10: {cedula_10}")
print(f"Quantidade de cédulas de R$1: {cedula_1}")
