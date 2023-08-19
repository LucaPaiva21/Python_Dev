'''
Desenvolva um programa que leia o primeiro termo e a razão de uma par.
No final, mostre os 10 primeiros termos dessa prograssão.
'''

primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite a razão da progressão: "))

print("Os 10 primeiros termos da progressão são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo)