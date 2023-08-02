class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self._titulo}, de {self._autor} ({self._ano_publicacao})"

    def imprimir_informacoes(self):
        print(f"Título: {self._titulo}")
        print(f"Autor: {self._autor}")
        print(f"Ano de Publicação: {self._ano_publicacao}")

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, novo_ano):
        self._ano_publicacao = novo_ano


def imprimir_livros_estante(livros):
    if not livros:
        print("\nA estante está vazia.")
    else:
        print("\n--- Livros na Estante ---")
        for idx, livro in enumerate(livros, 1):
            print(f"{idx}. {livro}")
        print("0. Voltar para o menu")


if __name__ == "__main__":
    livros = []
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar novo livro")
        print("2. Livros da estante")
        print("3. Sair")

        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        if escolha == "1":
            print("\nInsira os dados do livro:")
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = int(input("Ano de Publicação: "))

            livro = Livro(titulo, autor, ano_publicacao)
            livros.append(livro)

            print("\nInformações do livro:")
            livro.imprimir_informacoes()

        elif escolha == "2":
            while True:
                imprimir_livros_estante(livros)
                opcao_livro = input("Escolha um livro para ver as informações (0 para voltar): ")
                if opcao_livro == "0":
                    break
                try:
                    idx_livro = int(opcao_livro) - 1
                    livro_selecionado = livros[idx_livro]
                    print("\nInformações do livro selecionado:")
                    livro_selecionado.imprimir_informacoes()
                except IndexError:
                    print("Livro inválido. Escolha novamente.")

        elif escolha == "3":
            print("\nEncerrando o programa. Boa leitura e até mais!")
            break

        else:
            print("\nOpção inválida. Escolha novamente.")
