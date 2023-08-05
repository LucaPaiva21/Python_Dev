'''
Escreva um programa que pergunte o salário do funcionario
e calcule o valor do seu aumento

para salarios superiores a 1.250.00 calcule um aumento de 10%

para inferiores ou iguais, o aumento é de 15%
'''
salario = float(input("Informe seu salário: "))

if salario > 1250.00:
    aumento1 = salario * 0.10
    soma1 = salario + aumento1
    print(f"Seu salário é: {salario} reais.")
    print(f"Seu aumento é: {aumento1} reais.")
    print(f"Seu salário com o aumento é: {soma1} reais.")
if salario <= 1250.00:
    aumento2 = salario * 0.15
    soma2 = salario +aumento2
    print(f"Seu salário é: {salario} reais.")
    print(f"Seu aumento é: {aumento2} reais.")
    print(f"Seu salário com o aumento é: {soma2} reais.")