from modelos import Biblioteca
from excecoes import (LivroJaCadastradoError, LivroIndisponivelError, LivroNaoEncontradoError,
                      UsuarioJaCadastradoError, UsuarioNaoEncontrado, EmprestimoNaoEncontradoError,
                      DevolucaoError)


lib = Biblioteca()

def main():
    while True:
        print("BIBLIOTECA VIRTUAL")
        print("""1 - Cadastrar livro
2 - Cadastrar usuário
3 - Emprestar livro 
4 - Devolver livro
5 - Consultar livros 
6 - Relatório 
0 - Sair""")

        entrada = input("Digite um número correspondente: ")
        try:
            opt = int(entrada)
        except ValueError:
            print("Digite somente números inteiro entre 0 e 6.")
            continue
        if opt < 0 or opt > 6:
            print("Digite uma opção válida.")
            continue

# Sair do programa
        if opt == 0:
            break

# Cadastrar livro
        if opt == 1:
            titulo = str(input("Digite o nome do livro: ").strip())
            autor = str(input("Digite o autor: ").strip())
            try:
                ano = int(input("Digite o ano de lançamento: "))

                copias = int(input("Digite o número de cópias para cadastro: "))
            except ValueError:
                print("Digite somente números inteiros!")
                continue
            try:
                lib.cadastrar_livro(titulo=titulo, autor=autor, ano=ano, copias=copias)
                print("Livro cadastrado com sucesso!")
            except LivroJaCadastradoError as e:
                print(e)

# Cadastrar usuário
        if opt == 2:
            nome = str(input("Digite o nome de usuário: ").strip())
            try:
                id_usuario = int(input("Digite o id único de usuário: "))
            except ValueError:
                print("Digite somente números inteiros.")
                continue
            telefone = str(input("Digite o número de telefone: ").strip())
            try:
                lib.cadastrar_usuario(nome=nome, id_usuario=id_usuario, telefone=telefone)
                print("Usuário cadastrado com sucesso!")
            except UsuarioJaCadastradoError as e:
                print(e)
                    

if __name__ == "__main__":
    main()