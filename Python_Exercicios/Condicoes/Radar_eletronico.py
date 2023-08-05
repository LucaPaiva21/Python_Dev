'''
Escreva um programa que leia a velocidade de um carro.

se ele ultrapassar 80Km/h. Mostre uma mensagem dizendo que ele foi multado.

A multa vai custar 7 reais por cada km acima do limite
'''
velocidade = float(input("Quantos km você passou nessa pista?: "))

if velocidade > 80:
    excesso_e_velocidade = velocidade - 80
    multa = excesso_e_velocidade * 7
    print(f"Você ultrapassou o limite da avenida. Seu carro estava a {velocidade} Km/h.")
    print(f"Você estava {excesso_e_velocidade} km/h a mais do recomendado")
    print(f"Você tomará uma multa de 7 reais por km ultrapassado.\nSua multa é de: {multa} reais")
else:
    print(f"Tudo dentro dos conforme, meu chefe!")
