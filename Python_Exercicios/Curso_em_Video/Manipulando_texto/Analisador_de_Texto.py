'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas

- O nome com todas minúsculas

- Quantas letras ao todo(Sem considerar espaços)

- Quantas letras tem o primeiro nome
'''

# Nome completo do usúario
nome = str(input("Digite seu nome completo: "))

# Mostra o nome completo
print(f"Seu nome completo é: {nome}")

# Mostra o nome com todas as letras maiúsculas
print(f"Maiúsculo: {nome.upper()}") # Responsavel por imprimir toda a frase Maiúscula

# Mostra o nome com todas as letras minúsculas
print(f"Minúsculas: {nome.lower()}") # Responsavel por imprimir toda a frase Minúscula

# Mostra quantas letras tem, sem contar os espaços.
sem_espacos = nome.replace(" ", "") # Variável recebe o replace para substituir os espaços por uma str vazia
print(f"Quantidade de caracteres(sem contar os espaços): {len(sem_espacos)}")

# Mostrar quantas letrar tem o primeiro nome
Primeiro_nome = nome.split() # Usei o split para separar a frase, em varias listas
print(f"Seu primeiro nome tem: {len(Primeiro_nome[0])}") # Depois selecionei a lista do primeiro nome

