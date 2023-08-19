'''
Escreva um programa para aprovar um emprestimo bancario para compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario
ou então o emprestimo será negado
'''

valor_casa = float(input("Digite o valor da casa: "))
salario_comprador = float(input("Digite o salário do comprador: "))
anos_pagamento = int(input("Digite a quantidade de anos para pagamento: "))

prestacao_maxima = salario_comprador * 0.3
prestacao_mensal = valor_casa / (anos_pagamento * 12)

if prestacao_mensal <= prestacao_maxima:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R${prestacao_mensal}")
else:
    print("Empréstimo negado. Prestação excede 30% do salário.")
    print(f"Valor da prestação mensal: R${prestacao_mensal}")
    print(f"Prestação máxima permitida: R${prestacao_maxima}")





