'''
Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa, mostre:
A media de idade do grupo
Qual o nome do homem mais velho
Quantas mulheres tem menos de 20 anos
'''
soma_idades = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_de_20 = 0

for _ in range(4):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ").upper()
    
    soma_idades += idade
    
    if sexo == 'M' and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1

media_idades = soma_idades / 4

print(f"A média de idade do grupo é: {media_idades:.2f} anos.")
print(f"O nome do homem mais velho é: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_de_20}")
