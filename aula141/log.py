from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'



class Log:
    def _log(self, msg):
        raise NotImplementedError("Implemente o metodo log")
    
    def log_error(self, msg):
        return self._log(f'Erros: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucesso: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
         mensagem_formatada = f'{__class__.__name__} log via file: {msg}'
         print(f'Salvando {msg}')
         with open(LOG_FILE, 'a') as arquivo:
             arquivo.write(mensagem_formatada)
             arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{__class__.__name__} via print: {msg}')
    

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_sucess("Passou")
    lp.log_error('No passou')
    
    lf = LogFileMixin()
    lf.log_sucess('Passou no teste')
    lf.log_error('Erro no teste')
    
