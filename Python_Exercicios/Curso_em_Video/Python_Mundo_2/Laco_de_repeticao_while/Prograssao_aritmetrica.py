'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma pa, mostrando os 10
primeiros termos da prograssão usando a estrutura while.
'''

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termos_mostrados = 0
termo_atual = primeiro_termo

while termos_mostrados < 10:
    print(termo_atual, end=" ")
    termo_atual += razao
    termos_mostrados += 1

print("Fim da progressão aritmética.")