import pessoas
import contas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Contas] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def autorizar(self, cliente: pessoas.Pessoa, conta: contas.Contas):
        if conta.agencia in self.agencias and cliente in self.clientes and conta in self.contas:
            return True
        print("Nao autorizado")
        return False
        
    
    
    
    
if __name__ == "__main__":
    
    c1 = pessoas.Cliente('Felipe', 30)    
    cc1 = contas.ContaCorrente(agencia= 6, conta= 10, saldo= 200, limite=100)
    
    c1.conta = cc1
    
    
    banco = Banco()
    banco.clientes.extend([c1])
    banco.contas.extend([cc1])
    banco.agencias.extend([5])
    
    if banco.autorizar(c1, cc1):
        cc1.sacar(250)