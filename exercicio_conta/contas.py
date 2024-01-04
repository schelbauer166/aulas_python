import abc

class Conta(abc.ABC):
    def __init__(self, agencia, numero_conta, saldo) -> None:
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    @abc.abstractmethod
    def sacar(self, valor):
        ...

class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor >= self.saldo:
            print(f'Seu saldo é insuficiente, saldo: {self.saldo}, Valor para saque: {valor} voce esta usando seu limite.')
        self.saldo -= valor
        print(f'Seu saldo e de: {self.saldo}')
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor >= self.saldo:
            print(f'Saldo insuficiente, Saldo:{self.saldo} ')