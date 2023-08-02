'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média
'''

# Notas do aluno, informada por ele mesmo
nota1 = float(input("Digite a nota do 1° Bimestre: "))
nota2 = float(input("Digite a nota do 2° Bimestre: "))
nota3 = float(input("Digite a nota do 3° Bimestre: "))
nota4 = float(input("Digite a nota do 4° Bimestre: "))

# Variável responsavel pela média
media = (nota1 + nota2 + nota3 + nota4) / 4 
# A divisão vem primeiro que a soma, mas colocamos entre paraenteses a soma para ela virar preferencia.

# Mostra o resultado na tela para o usúario ver
print(f"Calculamos sua média, e o resultado é: {media}")