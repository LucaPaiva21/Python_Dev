'''
Existe 4 tipos primitivos padrôes na linguagem python
'''
int # Números inteiros = 7, -4, 0, 9875
float # Números reais = 7.0, -4.0, 0.0, 9875.0
bool # Valores booleanos = True, False
str # Texto = "Texto"

'''
Saída de dados
'''

# O mais padrão é
nome = "Luca"
print("Olá, sei que seu nome é:", nome)

# A segunda forma é
nome = "João"
print("Olá, eu sei que seu nome é {}".format(nome))

# A terceira e aque eu acho a mais simples é
nome = "Maria"
print(f"Olá, eu sei que seu nome é {nome}")

#Para você saber o tipo da variavel, é bem simples:

print(type("Olá, Mundo")) # Nesse caso vai sair esse resultado = type str

print(type(5)) # Nesse caso vai sair esse resultado = type int

print(type(5.5)) # Nesse caso vai sair esse resultado = type float

print(type(True)) # Nesse caso vai sair esse resultado = type bool

