import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self)  -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome
        
    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade: int) -> None:
        self._idade = idade
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Contas | None = None

    
  
    
        
        
        
    