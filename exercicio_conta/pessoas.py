import contas


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None
        



if __name__ == '__main__':
    
    c1 = Cliente('Felipe', 30)
    c1.conta = contas.ContaCorrente(10, 123, 200)
    
    c1.conta.depositar(500)
    print(c1.conta.saldo)