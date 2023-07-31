'''
Replicar informações usando aritmétrica
'''

nome1 = input("Digite seu nome: ")
print(f"Prazer em te conhecer {nome1:20}!")
# Escreve o nome dentro de 20 espaços

nome2 = input("Digite seu nome: ")
print(f"Prazer em te conhecer {nome2:>20}!")
# Escreve o nome dentro de 20 espaços para a direita

nome3 = input("Digite seu nome: ")
print(f"Prazer em te conhecer {nome3:<20}!")
# Escreve o nome em 20 espaços para esquerda

nome4 = input("Digite seu nome: ")
print(f"Prazer em te conhecer {nome4:^20}!")
# Escreve o nome centralizado dentro dos 20 espaços

nome5 = input("Digite seu nome: ")
print(f"Prazer em te conhecer {nome5:=^20}!")

'''
Infromações extras
'''
# Para quebra a linha do print usamos a seguite funçõa
nome6 = "Luca"
print(f"Olá, me chamo {nome6}! \n E você, como se chama?")

# caso você quer que não quebre a linha, usamos o seguinte

print("Olá mundo!", end= " ")
print("Como você tá?")