'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
altura = float(input("Digite sua altura(metros): "))

peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

print("="*40)
print(f"Sua altura é: {altura}\nPeso ideal para homem: {peso_homem}\nPeso ideal para mulher: {peso_mulher}")
print("="*40)
