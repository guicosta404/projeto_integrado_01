class Livro:
    def __init__(self, titulo, autor, ano, copias_totais, copias_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.copias_totais = copias_totais
        self.copias_disponiveis = copias_disponiveis

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

class LivroIndisponivelError(Exception):
    pass

l1 = Livro("HP", "JK", 2000, 2, 2)
l1.diminuir_copia()
l1.diminuir_copia()
l1.diminuir_copia()

