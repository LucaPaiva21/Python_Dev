'''
Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não.
No final, mostre:

a- quantas pessoas tem mais de 18 anos
b- quantos homens foram cadastrado
c- quantas mulheres tem menos de 20 anos
'''
pessoas_mais_de_18 = 0
homens_cadastrados = 0
mulheres_menos_de_20 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    
    if idade > 18:
        pessoas_mais_de_18 += 1
    
    if sexo == "M":
        homens_cadastrados += 1
    elif sexo == "F" and idade < 20:
        mulheres_menos_de_20 += 1
    
    continuar = input("Deseja continuar cadastrando? (S/N): ").upper()
    if continuar != "S":
        break

print(f"Quantidade de pessoas com mais de 18 anos: {pessoas_mais_de_18}")
print(f"Quantidade de homens cadastrados: {homens_cadastrados}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_de_20}")
