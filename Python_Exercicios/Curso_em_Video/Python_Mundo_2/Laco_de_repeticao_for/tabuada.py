'''
Refaça a atividade 9. Mostrando a tabuada de um número que o usúario escolher, so que
agora utilizando um laço for.
'''

numero = int(input("Digite um número de 1 a 10: "))

for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f"{numero}x{tabuada} = {resultado}")