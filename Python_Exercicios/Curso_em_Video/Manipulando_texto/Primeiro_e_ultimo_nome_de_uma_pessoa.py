'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e ultimo nome separadamente

ex:
nome = Ana Maria de Souza
primeiro = Ana
Ultimo = Souza
'''
nome = str(input("Digite seu nome completo: "))
primeiro = nome.split()
ultimo = nome.split()
print(f"Nome completo: {nome}")
print(f"Primeiro: {primeiro[0]}")
print(f"Ultimo: {ultimo[-1]}")