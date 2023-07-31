'''
Faça um programa que leia qualquer coisa, e descreva ela como variável.
'''
# Variável ao qual o usúario irá dissecar
x = input("Digite algo: ")

# Para ver que tipo primitivo a variável é
print(f"O tipo primitivo desse valor é {type(x)}")

# Se só contém espaços
print(f"Só tem espaços?: {x.isspace()}")

# Se é um número
print(f"É um número?: {x.isnumeric()}")

# Se só letras
print(f"É alfabético?: {x.isalpha()}")

# Se contém letras e números
print(f"É alfanumérico?: {x.isalnum()}")

# Se está totalmente maiúscula
print(f"Está em maiúscula?: {x.isupper()}")

# Se está totalmente minúscula
print(f"Está em minúsucla?: {x.islower()}")

# Se está com a primeira letra maiúscula
print(f"Está capitalizada?: {x.istitle()}")
