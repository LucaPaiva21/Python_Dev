'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

while "f" or "m":
    sexo = str(input("Digite seu sexo(m = Masculino, f = Feminino): "))
    if sexo == "m":
        print(f"Ta certo! Você digitou {sexo}, então seu sexo é masculino.")
    elif sexo == "f":
        print(f"Ta certo! Você digitou {sexo}, então seu sexo é feminino.")
    else:
        print("Sexo invalido, insira f ou m")
        