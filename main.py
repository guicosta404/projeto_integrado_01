from excecoes import LivroIndisponivelError, LivroJaCadastradoError, UsuarioJaCadastradoError


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

    def __str__(self):
        return f"- Título: {self.titulo}\n- Autor: {self.autor}\n- Ano de lançamento: {self.ano}"


class Usuario:
    def __init__(self, nome: str, id_usuario: int, telefone: str):
        self.nome = nome
        self.id_usuario = id_usuario
        self.telefone = telefone

    def __str__(self):
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

b = Biblioteca()
b.cadastrar_livro("jj", "jk", 2000, 2)
b.cadastrar_livro("jj", "jk", 2000, 2)