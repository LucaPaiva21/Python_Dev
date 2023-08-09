'''
Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome
"Santo"
'''

nome_cidade = str(input("Digite o nome da sua cidade: "))


print("Santo" in nome_cidade.split()[0])
