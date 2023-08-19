'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela
uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um segundo número inteiro: "))

if numero1 > numero2:
    print(f"O primeiro número é maior. {numero1} é maior que {numero2}")
elif numero2 > numero1:
    print(f"O segundo número é maior. {numero2} é maior que o número {numero1}")
elif numero1 == numero2 or numero2 == numero1:
    print(f"Não existe número maior, os dois são iguais. {numero1} é igual ao núemro {numero2}")
    