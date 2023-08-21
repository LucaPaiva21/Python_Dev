'''
Melhore o jogo da adivinhação, onde o computador vai "pensar" em um número entre 0 ou 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''
import random

numero = random.randint(0, 10)

print("Bem-vindo ao Jogo da Adivinhação!")
palpites = 0
acertou = False

while not acertou:
    chute = int(input("Digite um número de 0 a 10: "))

    if chute == numero:
        acertou = True
    else:
        print("Chute errado, Tente novamente.")
        palpites += 1

print(f"Parabéns! Você acertou em {palpites + 1} tentativas.")
