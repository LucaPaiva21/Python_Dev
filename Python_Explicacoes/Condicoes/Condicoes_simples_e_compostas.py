'''
Condições
'''

# if: = se - Bloco true
# else: = senão Bloco False

# Exemplo

tempo = int(input("Quantos anos tem seu carro?: "))

if tempo <= 3:
    print("Seu carro ta novo")
else:
    print("Carro Velhaço")
print("--FIM--")

nome = str(input("DIGITE SEU NOME: "))
if nome == "Leandro":
    print("Que nome lindo o seu!")
print(f"Bom dia, {nome}")

# Uma estrutura de condição simples, basta ter somente o if
# Caso tenha o else junto, se torna uma condição composta
