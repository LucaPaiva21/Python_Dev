'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles qe forem
pares. Se o valor digitado for impar, desconsidere-o.
'''
soma_pares = 0

for _ in range(6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        soma_pares += numero
print(f"A soma dos números pares é: {soma_pares}")
