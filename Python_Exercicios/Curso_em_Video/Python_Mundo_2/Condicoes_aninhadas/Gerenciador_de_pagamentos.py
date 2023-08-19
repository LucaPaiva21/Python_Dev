'''
Elabore um programa que calcule o valor a ser pago por um produto
considerando o seu preço normal e condição de pagamento:

- A vista dinheiro/cheque 10% de desconto
- A vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em até 3x no cartão: 20% de juros

'''

valor_produto = float(input("Informe qual o valor do produto: "))

print("Informe qual opção de pagamento")
print("="*40)
print("1- A vista no dinheiro/cheque (contem 10% de desconto)")
print("2- A vista no cartão (contem 5% de desconto)")
print("3- Em até 2x no cartão")
print("4- Em até 3x no cartão (contem juros)")
print("="*40)

escolha = int(input("Digite o número da opção: "))

desconto_de_10 = valor_produto * 0.10
desconto_de_05 = valor_produto * 0.05
juros = valor_produto * 1.2

if escolha == 1:
    print(f"Como você pagou a vista no dinheiro, o desconto foi aplicado. De {valor_produto}R$ vai para {valor_produto - desconto_de_10}R$")
elif escolha == 2:
    print(f"Como você pagou a vista no cartão, o desconto foi aplicado. De {valor_produto}R$ vai para {valor_produto - desconto_de_05}R$")
elif escolha == 3:
    print(f"Você pagou em 2x no cartão, o preço será normal: {valor_produto}R$. Dua parcelas de {valor_produto/2}")
elif escolha == 4:
    print(f"Você pagou em 3x no cartão, contém juros de 20%. De {valor_produto}R$ vai para {valor_produto + juros}R$ com 3 parcelas de {(valor_produto + juros)/3}R$")
