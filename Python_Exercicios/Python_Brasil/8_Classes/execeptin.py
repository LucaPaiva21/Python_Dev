class TrianguloInvalidoException(Exception):
    def __init__(self, mensagem="Os lados fornecidos não formam um triângulo válido."):
        super().__init__(mensagem)

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def verificar_triangulo(self):
        if self.ladoA + self.ladoB <= self.ladoC or \
           self.ladoA + self.ladoC <= self.ladoB or \
           self.ladoB + self.ladoC <= self.ladoA:
            raise TrianguloInvalidoException()

try:
    ladoA = float(input("Digite o valor do lado A: "))
    ladoB = float(input("Digite o valor do lado B: "))
    ladoC = float(input("Digite o valor do lado C: "))
    
    triangulo = Triangulo(ladoA, ladoB, ladoC)
    triangulo.verificar_triangulo()
    
    perimetro = triangulo.calcular_perimetro()
    print("É um triângulo válido!")
    print(f"Perímetro: {perimetro}")
except ValueError:
    print("Erro: Insira valores numéricos para os lados do triângulo.")
except TrianguloInvalidoException as ex:
    print(f"Erro: {ex}")
