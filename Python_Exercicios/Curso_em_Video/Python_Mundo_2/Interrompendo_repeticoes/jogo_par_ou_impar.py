'''
faça um programa que jogue par ou impar com o computador.
O jogo so sera interrompido quando o jogador perder.
Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''
import random

vitorias_consecutivas = 0

while True:
    jogador_escolha = input("Escolha par ou ímpar (p/i): ").lower()
    jogador_numero = int(input("Digite um número entre 0 e 10: "))
    
    if jogador_escolha not in ['p', 'i'] or jogador_numero < 0 or jogador_numero > 10:
        print("Escolha inválida. Tente novamente.")
        continue
    
    computador_numero = random.randint(0, 10)
    print(f"Computador escolheu o número {computador_numero}")
    
    total = jogador_numero + computador_numero
    resultado = "par" if total % 2 == 0 else "ímpar"
    
    print(f"Total: {total} ({resultado})")
    
    if (resultado == "par" and jogador_escolha == "p") or (resultado == "ímpar" and jogador_escolha == "i"):
        print("Você venceu!\n")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu.")
        break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")
