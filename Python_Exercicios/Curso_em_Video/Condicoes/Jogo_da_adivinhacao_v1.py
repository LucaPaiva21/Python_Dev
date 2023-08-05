'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o escolhido pelo computador

O programa deverá escrever na tela se o usúario venceu ou perdeu.
'''
import random

print("="*35)
print("Esse jogo foi feito para você tentar adivinhar!\nMe informe um número de 0 a 5.")
print("="*35)

numero = int(input("Digite um número de 0 a 5: "))
lista_de_numero = [0, 1, 2, 3, 4, 5]
numero_sorte = random.choice(lista_de_numero)

if numero == numero_sorte:
    print(f"UAU!!! Como você sabia que o número que eu escolhi foi {numero_sorte}???")
else:
    print("Caramba....você está sem sorte.")
    print(f"O número escolhido foi: {numero_sorte}")