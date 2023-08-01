'''
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro.
Faça um programa que ajude ele, lendo e escrevendo o nome escolhido
'''

import random

alunos = ["Leo", "Luca", "João", "Maria"]

print("Lista de alunos:")
for aluno in alunos:
    print(aluno)

# Sorteio do aluno
aluno_escolhido = random.choice(alunos)

print(f"Aluno escolhido: {aluno_escolhido}")