'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc
e mostre se status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade mórbida
'''

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu imc é: {imc}, você está abaixo do peso")
elif imc == 18.5 or imc < 25:
    print(f"Seu imc é: {imc}, você está com o peso ideal")
elif imc == 25 or imc < 30:
    print(f"Seu imc é: {imc}, você está sobrepeso")
elif imc == 30 or imc < 40:
    print(f"Seu imc é:{imc}, você está com obesidade mórbida")
