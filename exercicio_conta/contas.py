from abc import ABC, abstractmethod


class Contas(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        print(f'Voce deposiou R${valor}. Saldo atualizado R${self.saldo}')
        return self.saldo
    
    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass
    

class ContaPoupanca(Contas):
    
    def sacar(self, valor: float) -> float | None:
        if valor > self.saldo:
            print("Saldo insuficiente")
            return None
        saldo_atualizado = self.saldo - valor
        print(f'Saque autorizado, saldo: {saldo_atualizado}')
        return saldo_atualizado
    

class ContaCorrente(Contas):
    def __init__(self, agencia: int, conta: int, saldo: float, limite: float) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def sacar(self, valor: float) -> float:
        if valor > self.saldo:
            valor_ = valor - self.saldo
            saldo_final = self.limite - valor_
            print(f'Saldo insuficiente, utilizando {valor_} do seu limite.')
            return saldo_final
        return self.saldo - valor
    
    


    

    
        