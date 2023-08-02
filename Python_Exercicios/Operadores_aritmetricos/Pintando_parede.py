'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calucule a sua área e a quantidade de tinta necessaria para pinta-la.
sabendo que a cada litro de tinta, pinta uma área de 2m*2
'''

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
tinta = area / 2

print(f'A área da parede é de {area}m²')
print(f'Para pintar a parede, você precisará de {tinta} litros de tinta')
