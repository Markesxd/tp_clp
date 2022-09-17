from .Totalizavel import Totalizavel
from .Produto import Produto  
class ItemVenda(Totalizavel):
    def __init__(self):
        super().__init__()
        self.produto = Produto
        self.valor = 0.0
        self.quantidade = 0