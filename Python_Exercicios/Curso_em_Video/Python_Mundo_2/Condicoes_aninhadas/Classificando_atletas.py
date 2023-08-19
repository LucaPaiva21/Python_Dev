'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria de acordo com a idade

- ate 9 anos: mirim
- ate 14 anos: infantil
- ate 19 anos: junior
- ate 20 anos: senior
- acima: master
'''

ano = int(input("Digite o seu ano de nascimento: "))

ano_calculo = 2023 - ano

if ano_calculo <= 9:
    print("Sua categoria é: Mirim")
elif ano_calculo == 10 or ano_calculo <= 14:
    print("Sua categoria é: Infantil")
elif ano_calculo == 15 or ano_calculo <= 19:
    print("Sua categoria é: Junior")
elif ano_calculo == 20:
    print("Sua categoria é: Sênior")
elif ano_calculo > 20:
    print("Sua categoria é: Master")