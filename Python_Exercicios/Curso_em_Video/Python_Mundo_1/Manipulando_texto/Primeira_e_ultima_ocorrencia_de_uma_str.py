'''
Faça um programa que leia uma frase pelo teclado e mostre:

- Quantas vezes aparece a letra "a"

- Em que posição ela aparece a primeira vez

- Em que posição ela aparece a última vez
'''

frase = str(input("Digite uma fase: "))

contador_de_letras = frase.count("a")

primeira_vez = frase.find("a")
ultima_vez = frase.rfind("a")

print(f"sua frase tem: {contador_de_letras} letras a.")
print(f"A primeira letra a, apareceu: {primeira_vez}")
print(f"A ultima vez que apareceu: {ultima_vez}")