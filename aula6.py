class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    
    def adicionar_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    
    def listar_enderecos(self):
        for e in self.enderecos:
            print(e.rua, e.numero)
        
        



class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
        
pessoa1 = Cliente('felipe')
pessoa1.adicionar_endereco('sao joao', 20)
pessoa1.adicionar_endereco('centro', 30)
pessoa1.listar_enderecos()