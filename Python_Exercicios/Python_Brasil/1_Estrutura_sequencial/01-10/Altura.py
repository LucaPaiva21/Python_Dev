'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

print("="*30)
print("Vamos descobrir o seu peso ideal!")
print("="*30)

altura = float(input("Informe sua altura(em metros): "))

peso_homens = (72.7 * altura) - 58
peso_mulheres = (62.1 * altura) - 44.7

print("="*40)
print("Seu peso ideal é:")
print(f"Se você for homem, seu peso ideal é: {peso_homens}")
print(f"Se você for mulher, seu peso ideal é: {peso_mulheres}")
print("="*40)