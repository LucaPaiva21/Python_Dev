'''
O mesmo professor do desafio anterior
quer sortear a ordem de apresentação
de trabalhos dos alunos.
Faça um rpograma que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

# Ler os nomes dos 4 alunos
alunos = []
for i in range(4):
    nome_aluno = input(f"Digite o nome do {i+1}° aluno: ")
    alunos.append(nome_aluno)

# Sorteia a ordem dos alunos
random.shuffle(alunos)

# Mostra a ordem sorteada

for i in range(4):
    print(f"{i+1}° aluno: {alunos[i]}")
