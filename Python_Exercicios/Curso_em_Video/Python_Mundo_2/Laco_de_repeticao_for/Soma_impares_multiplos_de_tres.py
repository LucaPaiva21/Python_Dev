'''
Faça um programa que calcule a soma entre todos os números impares que
são multiplos de tres e que se encontram no intervalo de 1 ate 500
'''
soma = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero

print(f"A soma dos números é: {soma}")