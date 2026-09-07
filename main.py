from excecoes import LivroIndisponivelError


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

