'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

# Variaveis para a primeira pergunta
dobro = num1 * 2
dobro_com_a_metade = (num1 * 2) + num2 / 2

# Variaveis para a segunda pergunta
triplo = num1 * 3
soma_do_triplo = (num1 * 3) + num3

# Variaveis para a terceira pergunta
cubo = num3 **3

# Primeira pergunta
print("="*30)
print("Pergunta: O produto do dobro do primeiro com metade do segundo")
print(f"O produto é: {num1}")
print(f"O dobro é: {dobro}")
print(f"O produto do dobro do primeiro, com a metade do segundo é: {dobro_com_a_metade}")
print("="*30)

# Segunda pergunta
print("="*30)
print("Pergunta: A soma do triplo do primeiro com o terceiro")
print(f"O produto é: {num1}")
print(f"O triplo é: {triplo}")
print(f"A soma do triplo com o terceiro: {soma_do_triplo}")
print(f"="*30)

# Terceira pergunta
print(f"="*30)
print("Pergunta: A terceiro elevado ao cubo")
print(f"O produto do terceiro é: {num3}")
print(f"O terceiro elevado ao cubo é: {cubo}")
print("="*30)
