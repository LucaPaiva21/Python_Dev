'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

letra = input("Digite F ou M para seu sexo: ")

if letra == "F" or letra == "f":
    print("Seu sexo é feminino")
elif letra == "M" or letra == "m":
    print("Seu sexo é masculino")
else:
    print("Sexo inválido.")