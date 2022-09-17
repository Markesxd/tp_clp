from datetime import date
from .Totalizavel import Totalizavel
from .Cliente import Cliente

class Venda(Totalizavel):
    def __init__(self):
        super().__init__()
        self.numero = 0
        self.data = date.today()
        self.cliente = Cliente()
        self.itens = []

    def setNumero(self, numero):
        self.numero = numero

    def setAll(self):
        self.numero = int(input())
        data = input()
        [dia, mes, ano] = data.split('/')
        self.data = date(int(ano), int(mes), int(dia))

    def toString(self):
        return f"{self.numero}\n{self.data}"