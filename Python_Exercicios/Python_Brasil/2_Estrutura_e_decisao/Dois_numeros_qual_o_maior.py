'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

# Duas varáveis entregue pelo usúario
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Variável reponsável pelo número maior
maior = 0

# Decisão para mostrar qual dos dois é o maior
if numero1 > maior:
    maior = numero1
if numero2 > maior:
    maior = numero2

# Mostrar o resultado
print("="*40)
print(f"Os números apresentados foram:\nNúmero 1: {numero1}\nNúmnero 2: {numero2}")
print(f"O número maior entre eles foi o: {maior}")
print("="*40)
