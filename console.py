from modelos import Biblioteca, Livro, Usuario

lib = Biblioteca()

def main():
    while True:
        print("BIBLIOTECA VIRTUAL")
        print("\n1 - Cadastrar livro" \
        "\n2 - Cadastrar usuário" \
        "\n3 - Emprestar livro" \
        "\n4 - Devolver livro" \
        "\n5 - Consultar livros" \
        "\n6 - Relatórios" \
        "\n0 - Sair")

        entrada = input("Digite um número correspondente: ")
        try:
            opt = int(entrada)
        except ValueError:
            print("Digite somente números inteiro entre 0 e 6.")
            continue
        if opt < 0 or opt > 6:
            print("Digite uma opção válida.")
            continue       

        if opt == 0:
            break
if __name__ == "__main__":
    main()