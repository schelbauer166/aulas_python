from abc import ABC, abstractmethod


class Log(ABC):
    
    @abstractmethod
    def _log(self, msg):...
        
    
    def log_error(self, msg):
        return self._log(f'Erros: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucesso: {msg}')
    
    

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{__class__.__name__} via print: {msg}')
        
        
l1 = LogPrintMixin()
l1.log_sucess("teste")