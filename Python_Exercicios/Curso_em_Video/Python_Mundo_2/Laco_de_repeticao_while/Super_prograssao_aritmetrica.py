'''
Melhore o desafio numero 61, perguntando se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mstrar 0 termos.
'''
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termos_mostrados = 0
termo_atual = primeiro_termo

while True:
    qtd_termos = int(input("\nQuantos termos você quer mostrar? (Digite 0 para encerrar): "))
    
    if qtd_termos == 0:
        print("Encerrando o programa.")
        break
    
    while termos_mostrados < qtd_termos:
        print(termo_atual, end=" ")
        termo_atual += razao
        termos_mostrados += 1
    
    termos_mostrados = 0
    termo_atual = primeiro_termo
