'''
Faça um programa em Linguagem Python que leia
um valor inteiro e mostre a tabuada de 1 a 10 do valor lido. 
'''

print("="*40)
print("Tabuada")
print("="*40)

numero = int(input("Digite o número para ver a tabuada: "))

for tabuada in range(1, 11):
    print(numero,"x", tabuada, "=", (numero * tabuada))