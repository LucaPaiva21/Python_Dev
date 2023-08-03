import math

class Forma:
    def area(self):
        return 0

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area_retangulo(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area_circulo(self):
        return math.pi * self.raio ** 2

def main():
    while True:
        print("\nOpções:")
        print("1 - Calcular a área de um Retângulo")
        print("2 - Calcular a área de um Círculo")
        print("0 - Sair")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 0:
            print("Encerrando o programa.")
            break
        elif escolha == 1:
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            retangulo = Retangulo(base, altura)
            print(f"A área do retângulo é: {retangulo.area_retangulo()}")
        elif escolha == 2:
            raio = float(input("Digite o raio do círculo: "))
            circulo = Circulo(raio)
            print(f"A área do círculo é: {circulo.area_circulo()}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()