'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule
o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''
#50kg é o limite do estado de são Paulo
#Multa 4 reais por kilo a mais

#Input do peso do peixe
peso_do_peixe = float(input("Digite o peso do peixe: "))

#Variáveis para calcular o excesso
excesso = peso_do_peixe - 50
multa = excesso * 4

#Resultado para o usúario
print("="*40)
print(f"O peso do peixe foi: {peso_do_peixe}Kg\nO excesso foi: {excesso}Kg\nA multa foi: {multa}R$")
print("="*40)

