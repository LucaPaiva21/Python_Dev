'''
Faça um programa que mostre a tabuada de varios números, um de cada vez.
Cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitador for negativo.
'''
while True:
    numero = int(input("Digite um número (negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break
    
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")