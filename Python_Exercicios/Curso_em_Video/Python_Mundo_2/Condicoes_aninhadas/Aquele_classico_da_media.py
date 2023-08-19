'''
Crie um programa que leia duas notas de aluno e calcule sua média.
Mostrando uma mensagem no final de acordo com média atiginda:

- Média abaixo de 5.0:
Reprovado
- Média entre 5.0 e 6.9:
Recuperação
- Média 7.0 superior:
Aprovado
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f"Aprovado! Sua média foi: {media}")
elif media < 5.0:
    print(f"Você foi reprovado! Sua média é: {media}")
elif media <= 6.9 or media > 5.0:
    print(f"Você está de recuperação! Sua média foi: {media}")