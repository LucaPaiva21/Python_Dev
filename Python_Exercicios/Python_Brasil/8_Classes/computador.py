class PlacaMae:
    def __init__(self):
        self.modelo = None

    def selecionar_modelo(self):
        print("Modelos disponíveis de placa mãe:")
        print("1. Modelo A")
        print("2. Modelo B")
        print("3. Modelo C")
        opcao = int(input("Escolha o modelo da placa mãe (1-3): "))

        modelos = {
            1: "Modelo A",
            2: "Modelo B",
            3: "Modelo C",
        }

        self.modelo = modelos.get(opcao, "Modelo inválido")


class MemoriaRAM:
    def __init__(self):
        self.tipo = None
        self.quantidade_pentes = None
        self.capacidade_gigas = None

    def selecionar_tipo(self):
        print("Tipos de Memória RAM disponíveis:")
        print("1. DDR4")
        print("2. DDR5")
        opcao = int(input("Escolha o tipo de Memória RAM (1-2): "))

        tipos = {
            1: "DDR4",
            2: "DDR5",
        }

        self.tipo = tipos.get(opcao, "Tipo inválido")

    def selecionar_quantidade_pentes(self):
        self.quantidade_pentes = int(input("Digite a quantidade de pentes de Memória RAM (máximo 4): "))
        self.quantidade_pentes = min(self.quantidade_pentes, 4)

    def selecionar_capacidade_gigas(self):
        self.capacidade_gigas = []
        for pente in range(self.quantidade_pentes):
            gigas = int(input(f"Digite a capacidade em gigas do pente {pente + 1}: "))
            self.capacidade_gigas.append(gigas)


class MemoriaInterna:
    def __init__(self):
        self.tipos = ["SSD", "HD"]
        self.tipo_selecionado = None
        self.capacidade_gigas = None

    def selecionar_tipo(self):
        print("Tipos de Memória Interna disponíveis:")
        print("1. Somente SSD")
        print("2. Somente HD")
        print("3. Ambos (SSD e HD)")
        opcao = int(input("Escolha o tipo de Memória Interna (1-3): "))

        if 1 <= opcao <= 3:
            self.tipo_selecionado = self.tipos[opcao - 1]
        else:
            self.tipo_selecionado = "Tipo inválido"

    def selecionar_capacidade_gigas(self):
        self.capacidade_gigas = int(input("Digite a capacidade em gigas da Memória Interna: "))


class Processador:
    def __init__(self):
        self.marca = None
        self.versao = None

    def selecionar_marca(self):
        print("Marcas disponíveis de Processador:")
        print("1. Intel")
        print("2. AMD")
        opcao = int(input("Escolha a marca do Processador (1-2): "))

        marcas = {
            1: "Intel",
            2: "AMD",
        }

        self.marca = marcas.get(opcao, "Marca inválida")

    def selecionar_versao(self):
        print("Versões disponíveis do Processador:")
        if self.marca == "Intel":
            print("1. Versão 1")
            print("2. Versão 2")
            print("3. Versão 3")
        elif self.marca == "AMD":
            print("1. Versão A")
            print("2. Versão B")
            print("3. Versão C")

        opcao = int(input("Escolha a versão do Processador (1-3): "))

        if self.marca == "Intel":
            versoes = {
                1: "Versão 1",
                2: "Versão 2",
                3: "Versão 3",
            }
        elif self.marca == "AMD":
            versoes = {
                1: "Versão A",
                2: "Versão B",
                3: "Versão C",
            }

        self.versao = versoes.get(opcao, "Versão inválida")


class PlacaDeVideo:
    def __init__(self):
        self.modelo = None

    def selecionar_modelo(self):
        print("Modelos disponíveis de Placa de Vídeo:")
        print("1. Modelo X")
        print("2. Modelo Y")
        print("3. Modelo Z")
        opcao = int(input("Escolha o modelo da Placa de Vídeo (1-3): "))

        modelos = {
            1: "Modelo X",
            2: "Modelo Y",
            3: "Modelo Z",
        }

        self.modelo = modelos.get(opcao, "Modelo inválido")


class Cooler:
    def __init__(self):
        self.quantidade = None
        self.modelo = None

    def selecionar_quantidade(self):
        self.quantidade = int(input("Digite a quantidade de coolers (máximo 3): "))
        self.quantidade = min(self.quantidade, 3)

    def selecionar_modelo(self):
        print("Modelos disponíveis de Cooler:")
        print("1. Cooler A")
        print("2. Cooler B")
        print("3. Cooler C")
        opcao = int(input("Escolha o modelo do cooler (1-3): "))

        modelos = {
            1: "Cooler A",
            2: "Cooler B",
            3: "Cooler C",
        }

        self.modelo = modelos.get(opcao, "Modelo inválido")


class Fonte:
    def __init__(self):
        self.voltagem = None
        self.modelo = None

    def selecionar_voltagem(self):
        self.voltagem = float(input("Digite a voltagem da Fonte: "))

    def selecionar_modelo(self):
        print("Modelos disponíveis de Fonte:")
        print("1. Fonte Modelo 1")
        print("2. Fonte Modelo 2")
        print("3. Fonte Modelo 3")
        opcao = int(input("Escolha o modelo da Fonte (1-3): "))

        modelos = {
            1: "Fonte Modelo 1",
            2: "Fonte Modelo 2",
            3: "Fonte Modelo 3",
        }

        self.modelo = modelos.get(opcao, "Modelo inválido")


def exibir_especificacoes(computador):
    print("\n== Especificações do Computador ==")
    print(f"{'='*35}")
    print(f"Placa Mãe: {computador['Placa Mãe']}")
    print(f"Memória RAM:")
    print(f"   Tipo: {computador['Memória RAM']['Tipo']}")
    print(f"   Quantidade de Pentes: {computador['Memória RAM']['Quantidade de Pentes']}")
    for i, capacidade in enumerate(computador['Memória RAM']['Capacidade por Pente']):
        print(f"   Pente {i + 1}: {capacidade}GB")
    print(f"Memória Interna:")
    print(f"   Tipo: {computador['Memória Interna']['Tipo']}")
    print(f"   Capacidade: {computador['Memória Interna']['Capacidade']}GB")
    print(f"Processador:")
    print(f"   Marca: {computador['Processador']['Marca']}")
    print(f"   Versão: {computador['Processador']['Versão']}")
    print(f"Placa de Vídeo: {computador['Placa de Vídeo']}")
    print(f"Cooler:")
    print(f"   Quantidade: {computador['Cooler']['Quantidade']}")
    print(f"   Modelo: {computador['Cooler']['Modelo']}")
    print(f"Fonte:")
    print(f"   Voltagem: {computador['Fonte']['Voltagem']}V")
    print(f"   Modelo: {computador['Fonte']['Modelo']}")
    print(f"{'='*35}\n")

def main():
    computador = {}

    placa_mae = PlacaMae()
    placa_mae.selecionar_modelo()
    computador["Placa Mãe"] = placa_mae.modelo

    memoria_ram = MemoriaRAM()
    memoria_ram.selecionar_tipo()
    memoria_ram.selecionar_quantidade_pentes()
    memoria_ram.selecionar_capacidade_gigas()
    computador["Memória RAM"] = {
        "Tipo": memoria_ram.tipo,
        "Quantidade de Pentes": memoria_ram.quantidade_pentes,
        "Capacidade por Pente": memoria_ram.capacidade_gigas,
    }

    memoria_interna = MemoriaInterna()
    memoria_interna.selecionar_tipo()
    memoria_interna.selecionar_capacidade_gigas()
    computador["Memória Interna"] = {
        "Tipo": memoria_interna.tipo_selecionado,
        "Capacidade": memoria_interna.capacidade_gigas,
    }

    processador = Processador()
    processador.selecionar_marca()
    processador.selecionar_versao()
    computador["Processador"] = {
        "Marca": processador.marca,
        "Versão": processador.versao,
    }

    placa_video = PlacaDeVideo()
    placa_video.selecionar_modelo()
    computador["Placa de Vídeo"] = placa_video.modelo

    cooler = Cooler()
    cooler.selecionar_quantidade()
    cooler.selecionar_modelo()
    computador["Cooler"] = {
        "Quantidade": cooler.quantidade,
        "Modelo": cooler.modelo,
    }

    fonte = Fonte()
    fonte.selecionar_voltagem()
    fonte.selecionar_modelo()
    computador["Fonte"] = {
        "Voltagem": fonte.voltagem,
        "Modelo": fonte.modelo,
    }

    exibir_especificacoes(computador)

if __name__ == "__main__":
    main()
