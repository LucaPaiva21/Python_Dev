class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.salario = 0.0

    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Salário:", self.salario)


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo

    def informacoes_funcionario(self):
        self.mostrar_informacoes()
        print("Cargo:", self.cargo)

    def calculo_horaextra(self, horas):
        valor_horaextra = 15.00
        self.salario += valor_horaextra * horas


class Gerente(Pessoa):
    def __init__(self, nome, cpf, setor):
        super().__init__(nome, cpf)
        self.setor = setor
        self.quantidade_equipe = 0

    def informacoes_gerente(self):
        self.mostrar_informacoes()
        print("Setor:", self.setor)
        print("Quantidade de Equipe:", self.quantidade_equipe)

    def calculo_bonificacao(self):
        if self.quantidade_equipe >= 10:
            self.salario *= 1.10
        else:
            self.salario *= 1.05


def main():
    nome = input("Digite o nome da pessoa: ")
    cpf = input("Digite o CPF da pessoa: ")
    pessoa = Pessoa(nome, cpf)

    cargo = input("Digite o cargo do funcionário: ")
    funcionario = Funcionario(nome, cpf, cargo)

    setor = input("Digite o setor do gerente: ")
    gerente = Gerente(nome, cpf, setor)

    salario = float(input("Digite o salário da pessoa: "))
    pessoa.salario = salario
    funcionario.salario = salario
    gerente.salario = salario

    print("\nInformações da Pessoa:")
    pessoa.mostrar_informacoes()

    print("\nInformações do Funcionário:")
    funcionario.informacoes_funcionario()
    horas_extras = float(input("Digite a quantidade de horas extras trabalhadas pelo funcionário: "))
    funcionario.calculo_horaextra(horas_extras)
    print("Salário com horas extras:", funcionario.salario)

    print("\nInformações do Gerente:")
    gerente.informacoes_gerente()
    quantidade_equipe = int(input("Digite a quantidade de pessoas na equipe do gerente: "))
    gerente.quantidade_equipe = quantidade_equipe
    gerente.calculo_bonificacao()
    print("Salário com bonificação:", gerente.salario)


if __name__ == "__main__":
    main()
