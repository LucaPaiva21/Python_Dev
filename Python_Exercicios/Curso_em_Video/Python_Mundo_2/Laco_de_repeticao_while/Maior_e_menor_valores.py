'''
Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução,
mostre a media entre todos os maior e menor valores lidos. O programa deve
perguntar ao usuário se ele quer u não continuar a digitar valores.
'''
maior_valor = float('-inf')
menor_valor = float('inf')
soma_valores = 0
contador_valores = 0

while True:
    numero = int(input("Digite um número inteiro (ou digite 0 para parar): "))
    
    if numero == 0:
        break
    
    if numero > maior_valor:
        maior_valor = numero
    if numero < menor_valor:
        menor_valor = numero
    
    soma_valores += numero
    contador_valores += 1
    
    continuar = input("Deseja continuar? (S para sim, qualquer outra tecla para não): ")
    if continuar.lower() != 's':
        break

if contador_valores > 0:
    media = soma_valores / contador_valores
    print(f"Maior valor: {maior_valor}")
    print(f"Menor valor: {menor_valor}")
    print(f"Média entre maiores e menores valores: {media}")
else:
    print("Nenhum número foi digitado.")
