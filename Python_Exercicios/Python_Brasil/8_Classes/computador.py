class PlacaMae:
    def __init__(self):
        self.modelo = None

    def selecionar_modelo(self):
        print("Modelos disponíveis de placa mãe:")
        print("1. MSI MAG Z690 Tomahawk WIFI")
        print("2. ASUS PRIME Z790-A WIFI DDR5")
        print("3. Mainboard ASUS ROG X570 Crosshair VIII Hero")
        opcao = int(input("Escolha o modelo da placa mãe (1-3): "))

        modelos = {
            1: "MSI MAG Z690 Tomahawk WIFI",
            2: "ASUS PRIME Z790-A WIFI DDR5",
            3: "Mainboard ASUS ROG X570 Crosshair VIII Hero",
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
            print("1. VIntel Core i9-7980XE")
            print("2. Intel Core i7-9700k")
            print("3. Intel Core i5 9600K")
        elif self.marca == "AMD":
            print("1. AMD Ryzen 7 5800X")
            print("2. AMD Athlon Dual Core")
            print("3. AMD 5 5600X")

        opcao = int(input("Escolha a versão do Processador (1-3): "))

        if self.marca == "Intel":
            versoes = {
                1: "Intel Core i9-7980XE",
                2: "Intel Core i7-9700k",
                3: "Intel Core i5 9600K",
            }
        elif self.marca == "AMD":
            versoes = {
                1: "AMD Ryzen 7 5800X",
                2: "AMD Athlon Dual Core",
                3: "AMD 5 5600X",
            }

        self.versao = versoes.get(opcao, "Versão inválida")


class PlacaDeVideo:
    def __init__(self):
        self.modelo = None

    def selecionar_modelo(self):
        print("Modelos disponíveis de Placa de Vídeo:")
        print("1. GeForce RTX 4090")
        print("2. AMD Radeon RX 6900 XT")
        print("3. Nvidia GeForce RTX 3090 Ti")
        opcao = int(input("Escolha o modelo da Placa de Vídeo (1-3): "))

        modelos = {
            1: "GeForce RTX 4090",
            2: "AMD Radeon RX 6900 XT",
            3: "Nvidia GeForce RTX 3090 Ti",
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
        print("1. Noctua NH-D15")
        print("2. Air Master Hyper 212 RGB")
        print("3. Cooler Master MasterAir MA410M")
        opcao = int(input("Escolha o modelo do cooler (1-3): "))

        modelos = {
            1: "Noctua NH-D15",
            2: "Air Master Hyper 212 RGB",
            3: "Cooler Master MasterAir MA410M",
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
        print("1. Corsair RM850x")
        print("2. Corsair HX1000-1000W")
        print("3. Cooler Master Elite V3 Full Range 300W")
        opcao = int(input("Escolha o modelo da Fonte (1-3): "))

        modelos = {
            1: "Corsair RM850x",
            2: "Corsair HX1000-1000W",
            3: "Cooler Master Elite V3 Full Range 300W",
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
