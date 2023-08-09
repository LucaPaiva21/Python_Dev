'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
'''
p1 = float(input("Digite o preço do primeiro produto: "))
p2 = float(input("Digite o preço do segundo produto: "))
p3 = float(input("Digite o preço do terceiro produto: "))

mais_barato = 0

if p1 > mais_barato:
    mais_barato = p1
if p2 < mais_barato:
    mais_barato = p2
if p3 < mais_barato:
    mais_barato = p3


print("="*40)
print(f"O produto mais barato custa: {mais_barato} R$")
print("="*40)
