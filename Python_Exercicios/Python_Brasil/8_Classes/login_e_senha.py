import getpass

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
    
    def validar_senha(self):
        if len(self.senha) < 8:
            raise ValueError("A senha deve conter pelo menos 8 caracteres.")
        
        contem_letra_maiuscula = any(c.isupper() for c in self.senha)
        if not contem_letra_maiuscula:
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        
        contem_numero = any(c.isdigit() for c in self.senha)
        if not contem_numero:
            raise ValueError("A senha deve conter pelo menos um número.")
        

def main():
    login = input("Insira o login: ")
    senha = getpass.getpass("Insira a senha: ")
    
    usuario = Usuario(login, senha)
    
    try:
        usuario.validar_senha()
        print("Senha válida. Usuário criado com sucesso.")
    except ValueError as e:
        print(f"Erro: {e}")
    

if __name__ == "__main__":
    main()
