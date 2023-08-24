'''
Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguntar se o usuario vai continuar.
no final, mostre:

a- qual é o total gasto na compre
b- quantos produtos custam mais de 1000 reais
c- qual pe o nome do produto mais barato
'''
total_gasto = 0
produtos_mais_de_1000 = 0
produto_mais_barato = None
preco_mais_barato = float('inf')

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        produtos_mais_de_1000 += 1
    
    if preco_produto < preco_mais_barato:
        produto_mais_barato = nome_produto
        preco_mais_barato = preco_produto
    
    continuar = input("Deseja continuar cadastrando produtos? (S/N): ").upper()
    if continuar != "S":
        break

print(f"Total gasto na compra: R${total_gasto:.2f}")
print(f"Quantidade de produtos que custam mais de R$1000: {produtos_mais_de_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")
