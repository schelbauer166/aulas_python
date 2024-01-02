from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, nome) -> None:
        self.nome = nome
       
    @abstractmethod 
    def enviar(self) -> bool:
        ...

    
class NotificacaoSMS(Notificacao):
    
    def enviar(self) -> bool:
        print("Enviando SMS....")
        return True
    

class NotificacaoEmail(Notificacao):
    
    def enviar(self) -> bool:
        print("Enviando EMAIL...")
        return True
    
    
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print("Verdadeiro")
    else:
        print('False')
    
    

n1 = NotificacaoEmail("Nome")


notificar(n1)

