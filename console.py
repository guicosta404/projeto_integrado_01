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
            id_usuario = str(input("Digite o id único de usuário: ").strip())
            telefone = str(input("Digite o número de telefone: ").strip())
            try:
                lib.cadastrar_usuario(nome=nome, id_usuario=id_usuario, telefone=telefone)
                print("Usuário cadastrado com sucesso!")
            except UsuarioJaCadastradoError as e:
                print(e)

# Emprestar livro
        if opt == 3:
            id_usuario = str(input("Digite seu id: ").strip())
            titulo = str(input("Digite o nome do livro: ").strip())
            try:
                lib.emprestar_livro(id_usuario=id_usuario, titulo=titulo)
                print("Empréstimo realizado com sucesso.")
            except (LivroNaoEncontradoError, UsuarioNaoEncontrado, LivroIndisponivelError) as e:
                print(e)

# Devolver livro
        if opt == 4:
            id_usuario = str(input("Digite seu id: ").strip())
            titulo = str(input("Digite o nome do livro: ").strip())
            try:
                lib.devolver_livro(id_usuario=id_usuario, titulo=titulo)
                print("Livro devolvido com sucesso.")
            except (DevolucaoError, EmprestimoNaoEncontradoError) as e:
                print(e)

# Consultar
        if opt == 5:
            print("""Consultar:
1 - Ano de lançamento
2 - Título do livro
3 - Autor(a)
4 - Consultar usuário 
0 - Sair""")
            try:
                escolha = int(input("Digite a opção: "))
            except ValueError:
                print("Digite somente números.")
                continue
            if escolha == 1:
                try:
                    ano = int(input("Digite o ano de lançamento: "))
                    result = lib.consultar_ano(ano=ano)
                    if result:
                        print(result)
                    else: 
                        print(f"Nenhum livro encontrado com lançamento em {ano}")
                except ValueError:
                    print("Digite somente números inteiros.")

            if escolha == 2:
                titulo = str(input("Digite o título do livro: "))
                try:
                    print(lib.consultar_titulo(titulo=titulo))
                except LivroNaoEncontradoError as e:
                    print(e)     
    
            if escolha == 3:
                autor =  str(input("Digite o nome do autor(a): "))
                result = lib.consultar_autor(autor=autor)
                if result:
                    print(result)
                else:
                    print(f"Nenhum livro encontrado para o autor {autor}.")    

            if escolha == 4:
                id_usuario = str(input("Digite o id do usuário: ").strip())
                try:
                    print(lib.consultar_usuario(id_usuario=id_usuario))
                except UsuarioNaoEncontrado as e:
                    print(e)
                
# Relatório


if __name__ == "__main__":
    main()