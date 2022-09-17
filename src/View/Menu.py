class Menu(object):
    def main(self):
        print("--Menu--")
        print("1. Venda")
        print("2. Cliente")
        print("3. Produto")
    
    def entity(self, entity):
        print(f"--{entity}--")
        print(f"1. Nova {entity}")
        print(f"2. listar {entity}")
        print(f"3. alterar {entity}")
        print(f"4. deletar {entity}")
