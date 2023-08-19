'''
Escreva um programa que leia um número inteiro qualquer e peça para o usúario
escolher qual será a base de conversão

-1 para binario
-2 para octal
-3 para hexadecimal
'''
numero = int(input("Digite um número inteiro qualquer: "))
print("Escolha para qual você quer converter:")
print("1- Binario")
print("2- Octal")
print("3- Hexadecimal")
escolha = int(input("Esolha qual deles: "))

numero_binario = bin(numero)
numero_octal = oct(numero)
numero_hexadecimal = hex(numero)

if escolha == 1:
    print(f"Convertendo....")
    print(f"A conversão do número {numero} para binario é: {numero_binario}")
if escolha == 2:
    print(f"Convertendo....")
    print(f"A conversão do número {numero} para octal é: {numero_octal}")
if escolha == 3:
    print(f"Convertendo....")
    print(f"A conversão do número {numero} para hexadecimal é: {numero_hexadecimal}")