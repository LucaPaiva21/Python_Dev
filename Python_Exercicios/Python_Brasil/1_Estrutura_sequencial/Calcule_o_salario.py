'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''
ganha_por_hora = float(input("Quanto você ganha por hora?: "))
hora_trabalhada = float(input("Quantas horas você trabalha?: "))
dias_do_mes = int(input("Quantas vezes do mês você trabalhou(dias): "))
salario = (ganha_por_hora * hora_trabalhada) * dias_do_mes

print(f"Você trabalhou: {dias_do_mes} dias.\nTrabalhou: {hora_trabalhada} horas por dia.\nVocê ganha: {ganha_por_hora} reais por hora.\nSeu alário desde mês é: {salario} reais.")
print("Se divirta com esse dinheiro!")