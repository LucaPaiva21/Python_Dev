'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print("O número não é primo.")
else:
    eh_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print("O número é primo.")
    else:
        print("O número não é primo.")

