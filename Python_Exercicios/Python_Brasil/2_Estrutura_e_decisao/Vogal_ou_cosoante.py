'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

# Letra entregue pelo usúario
letra = input("Digite uma letra: ")

# Vogais, lista para auxiliar nas decisões
vogais = ["a", "e", "i", "o", "u"]

# Decisão
if letra in vogais: #Conferindo se a letra esta presente na lista vogais
    print(f"A letra {letra}, é uma vogal.")
else: #Caso não esteja na lista vogal, será considerada consoante.
    print(f"A letra {letra}, é uma consoante.")
