from excecoes import (LivroIndisponivelError, LivroJaCadastradoError,
                       UsuarioJaCadastradoError, LivroNaoEncontradoError,
                       UsuarioNaoEncontrado, EmprestimoNaoEncontradoError,
                       DevolucaoError)


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int, copias_totais: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias_totais = copias_totais
        self.copias_disponiveis = copias_totais

    def estou_disponivel(self):
        if self.copias_disponiveis <= 0:
            return False

        return True

    def diminuir_copia(self):
        if not self.estou_disponivel():
            raise LivroIndisponivelError(f"{self.titulo} não está disponível.")
        self.copias_disponiveis -= 1

    def aumentar_copia(self):
        if self.copias_disponiveis >= self.copias_totais:
            raise DevolucaoError("Erro na devolução.")
        self.copias_disponiveis += 1    

    def __repr__(self):
        return f"- Título: {self.titulo}\n- Autor: {self.autor}\n- Ano de lançamento: {self.ano}\n - Copias disponíveis: {self.copias_disponiveis}"


class Usuario:
    def __init__(self, nome: str, id_usuario: int, telefone: str):
        self.nome = nome
        self.id_usuario = id_usuario
        self.telefone = telefone

    def __repr__(self):
        return f"Nome: {self.nome} - ID: {self.id_usuario} - Tel.: {self.telefone}"


class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.emprestimos = {}

    def cadastrar_livro(self, titulo, autor, ano, copias):
        if titulo in self.livros:
            raise LivroJaCadastradoError(f"Livro {titulo} já cadastrado")
        novo_livro = Livro(titulo=titulo, autor=autor, ano=ano, copias_totais=copias)
        self.livros[titulo] = novo_livro

    def cadastrar_usuario(self, nome, id_usuario, telefone):
        if id_usuario in self.usuarios:
            raise UsuarioJaCadastradoError(f"ID {id_usuario} já cadastrado.")
        novo_usuario = Usuario(nome=nome, id_usuario=id_usuario, telefone=telefone)
        self.usuarios[id_usuario] = novo_usuario

    def consultar_titulo(self, titulo):
        if titulo in self.livros:
            return self.livros[titulo]
        raise LivroNaoEncontradoError(f"Livro {titulo} não encontrado.")

    def consultar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario]
        raise UsuarioNaoEncontrado(f"Usuario {id_usuario} não encontrado.")

    def emprestar_livro(self, id_usuario, titulo):
        livro = self.consultar_livro(titulo=titulo)
        usuario = self.consultar_usuario(id_usuario=id_usuario)
        livro.diminuir_copia()
        emprestimo = {"usuario": usuario, "livro": livro}
        self.emprestimos[(id_usuario, titulo)] = emprestimo
        return emprestimo

    def devolver_livro(self, id_usuario, titulo):
        if (id_usuario, titulo) not in self.emprestimos:
            raise EmprestimoNaoEncontradoError("Emprestimo não encontrado.")
        registro = self.emprestimos.pop((id_usuario, titulo))
        livro = registro["livro"]
        livro.aumentar_copia()

    def consultar_autor(self, autor):
        lista = []
        for livro in self.livros.values():
            if autor == livro.autor:
                lista.append(livro)
        return lista

    def consultar_ano(self, ano):
        lista = []
        for livro in self.livros.values():
            if ano == livro.ano:
                lista.append(livro)
        return lista

    def relatorio_emprestados(self):
        return list(self.emprestimos.values())

    def relatorio_disponiveis(self):
        disponiveis = []
        for livro in self.livros.values():
            if livro.estou_disponivel():
                disponiveis.append(livro)
        return disponiveis

    def relatorio_usuarios(self):
        return list(self.usuarios.values())