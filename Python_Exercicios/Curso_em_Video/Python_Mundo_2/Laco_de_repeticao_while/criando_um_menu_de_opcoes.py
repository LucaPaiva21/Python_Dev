'''
Crie um programa que leia dois valores e mostre um menu na tela:
1- somar
2- multiplicar
3- maior
4- novos números
5- sair do programa
seu programa deerá realizar a opreção realizada em cada caso
'''

sair = False

while not sair:
    n1 = int(input("Digite um valor: "))
    n2 = int(input("Digite um segundo número: "))
    print("Selecione o que você quer fazer:\n1- Somar\n2- Multiplicar\n3- Maior\n4- Novos números\n5- Sair")
    escolha = int(input("Digite o que quer fazer(numero): "))
    if escolha == 1:
        soma = n1 + n2
        print(f"A soma do número {n1} e número {n2} é: {soma}")
    elif escolha == 2:
        multiplicacao = n1 * n2
        print(f"A multiplicação do número {n1} e número {n2} é: {multiplicacao}")
    elif escolha == 3:
        maior = max(n1, n2)
        print(f"O maior número entre {n1} e {n2} é: {maior}")
    elif escolha == 4:
        sair = False
    elif escolha == 5:
        sair = True
print("Obrigado por usar")