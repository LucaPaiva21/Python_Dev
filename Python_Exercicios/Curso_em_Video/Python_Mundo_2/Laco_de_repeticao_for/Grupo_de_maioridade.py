'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date

ano_atual = date.today().year
maioridade = 18

menores = 0
maiores = 0

for _ in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento
    
    if idade < maioridade:
        menores += 1
    else:
        maiores += 1

print(f"{menores} pessoa(s) ainda não atingiram a maioridade.")
print(f"{maiores} pessoa(s) já são maiores de idade.")