'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
lidos.
'''
maior_peso = float('-inf')  # Inicializa o maior peso com um valor negativo infinito
menor_peso = float('inf')   # Inicializa o menor peso com um valor positivo infinito

for _ in range(5):
    peso = float(input("Digite o peso da pessoa: "))
    
    if peso > maior_peso:
        maior_peso = peso
    
    if peso < menor_peso:
        menor_peso = peso

print(f"O maior peso lido foi {maior_peso:.2f} kg.")
print(f"O menor peso lido foi {menor_peso:.2f} kg.")