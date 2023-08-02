'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''
ganha_por_hora = float(input("Quanto você ganha por hora?: "))
hora_trabalhada = float(input("Quantas horas você trabalha?: "))

salario = (ganha_por_hora * hora_trabalhada) * 21

print(f"Você trabalha {hora_trabalhada}")