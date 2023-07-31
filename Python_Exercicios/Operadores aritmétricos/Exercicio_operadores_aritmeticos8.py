'''
Faça um algoritimo que leia o preço de um produto e mostre seu preço
com 5% de desconto
'''

preco_produto = float(input("Digite o valor do produto: "))

desconto = preco_produto - (preco_produto * 0.05)

print(f"O produto custa R${preco_produto} e com desconto de 5% fica R${desconto}")