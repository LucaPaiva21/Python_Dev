'''
Praticando
'''

# Fatiando

frase = "Curso em Vídeo Python" # Frase de modelo


print(frase[3]) # Vai me mostar o espaço 3, no caso, a letra: "s"
print(frase[3: 13]) # Vai me mostrar do espaço 3, até o espaço 12: "so em Víde"
print(frase[3: 20: 2]) # Vai me mostrar do espaço 3, até o 19, pulando de 2 em 2: "s mVdoPto"

# Caso queria escrever um texto grande que copio na internet
# Basta usar aspas tripla:

print("""Olá, me chamo Luca e tenho 20 anos. Atualmente estou estudando
em um cuso no senac e tambem com o professor gustavo guanabara.
Sou atleta de porra nenhuma, porque sou ruim em tudo.""")
# Bastar colocar print no começo, abrir o parenteses, e colocar 3 aspas.
# Depois vai no final da frase, coloca 3 aspas de novo e fechar os parenteses
# Pronto, sua frase ja esta sendo printada para o usuario

print(len(frase))
print(frase.count("o"))
print(frase.find("deo"))
"Curso" in frase
