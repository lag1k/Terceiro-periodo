class Produto:
    def __init__(self, nome, preco, quantidade_estoque, categoria):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.categoria = categoria

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade):
        if self.quantidade_estoque >= quantidade:
            self.quantidade_estoque -= quantidade
        else:
            print("Quantidade insuficiente em estoque.")

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

# Exemplo de uso da classe Produto:
produto1 = Produto("Camiseta", 50.0, 100, "Vestuário")
print(f"Produto: {produto1.nome}, Preço: R${produto1.preco:.2f}, Estoque: {produto1.quantidade_estoque}, Categoria: {produto1.categoria}")

produto1.adicionar_estoque(50)
produto1.remover_estoque(20)
produto1.aplicar_desconto(10)

print(f"Novo preço após desconto: R${produto1.preco:.2f}")
