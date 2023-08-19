'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou o prazo do alistamento

seu programa também devera mostrar o tempo que faltou ou passou do prazo
'''

idade = int(input("Digite sua idade para informar sua situação no alistamento: "))

antes_do_prazo = 18 - idade
depois_do_prazo = idade - 18

if idade < 18:
    print(f"Não está no prazo de se alistar, falta: {antes_do_prazo} ano(s)")
elif idade == 18:
    print(f"Está na hora de se alistar!")
elif idade > 18:
    print(f"Já passou o prazo para se alistar, ja se passou: {depois_do_prazo} ano(s)")
