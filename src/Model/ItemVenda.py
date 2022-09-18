from .Totalizavel import Totalizavel
from .Produto import Produto  

class ItemVenda(Totalizavel):
    def __init__(self):
        super().__init__()
        self.produto = Produto()
        self.valor = 0.0
        self.quantidade = 0

    def setProduto(self, produto):
        self.produto = produto
        self.valor = self.produto.getValor()
        return self
    
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
        return self

    def getNome(self):
        return self.produto.getNome()

    def getQuantidade(self):
        return self.quantidade