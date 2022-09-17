
class Totalizavel(object):
    def total(self):
        if(self.itens == None):
            return self.valor * self.quantidade
        else:
            sum = 0
            for item in self.itens:
                sum += item.total()
            return sum
            