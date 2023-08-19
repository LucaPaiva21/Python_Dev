'''
Crie um programa que faça o computador jogar jokenpo com você.
'''
import random

opcoes = ["pedra", "papel", "tesoura"]

print("="*40)
print("Vamos jogar Pedra, Papel e Tesoura.")
print("Esolha um deles e tente ganhar da maquina.")
sua_escolha = input("Escoha alguma opção: ")
print("="*40)

escolha_maquina = random.choice(opcoes)

print("A maquina ja escolheu!")

# vitoria ou empate
if escolha_maquina == "pedra" and sua_escolha == "tesoura":
    print("A maquina escolheu pedra e você escolheu tesoura, você perdeu!")
elif escolha_maquina == "pedra" and sua_escolha == "papel":
    print("A maquina escolheu pedra e você escolheu papel, você ganhou!")
elif escolha_maquina == "pedra" and sua_escolha == "pedra":
    print("A maquina escolheu pedra e você tambem, deu empate.")
elif escolha_maquina == "papel" and sua_escolha == "tesoura":
    print("A maquinha escolheu papel e você escolheu tesoura, você ganhou!")
elif escolha_maquina == "papel" and sua_escolha == "papel":
    print("A maquinha escolheu papel e você tambem, deu empate.")
elif escolha_maquina == "paple" and sua_escolha == "pedra":
    print("A maquina escolheu papel e você escolheu pedra, você ganhou!")
elif escolha_maquina == "tesoura" and sua_escolha == "pedra":
    print("A maquinha escolheu tesoura e você escolheu pedra, você ganhou.")
elif escolha_maquina == "tesoura" and sua_escolha == "papel":
    print("A maquina escolheu tesoura e você escolheu papel, você perdeu!")
elif escolha_maquina == "tesoura" and sua_escolha == "tesoura":
    print("A maquina escolheu tesoura e você tambem, deu empate.")
