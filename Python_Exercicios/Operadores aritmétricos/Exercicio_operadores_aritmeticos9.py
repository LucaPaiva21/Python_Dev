'''
Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento
'''
salario = float(input("Digite seu salário: "))

novo_salario = salario + (salario * 15 / 100)

print(f"O seu novo salário é de R${novo_salario}")
