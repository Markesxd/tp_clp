from datetime import date
from .Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self):
        self.rg = ''
        self.DataDeNascimento = date