from ..Model.Venda import Venda
from ..Model.Cliente import Cliente
from ..Model.Produto import Produto
from ..View.Menu import Menu

class MenuController(object):

    def show(self):
        menu = Menu()      
        while True:
            menu.main()
            self.entity = input()
            menu.entity(self.switchEntity())
            self.action = input()
            self.entityClass = self.switchClass()
            self.switchAction()


    def switchEntity(self):
        if(self.entity == '1'):
            return 'Venda'
        elif(self.entity == '2'):
            return 'Cliente'
        elif(self.entity == '3'):
            return 'Produto'
        else:
            return 'Error'

    def switchClass(self):
        if(self.entity == '1'):
            return Venda()
        elif(self.entity == '2'):
            return Cliente()
        elif(self.entity == '3'):
            return Produto()
        else:
            return 'Error'

    def switchAction(self):
        if(self.action == '1'):
            self.entityClass.setAll()
        elif(self.action == '2'):
            print(self.entityClass.toString())
        elif(self.action == '3'):
            return Produto
        else:
            return 'Error'