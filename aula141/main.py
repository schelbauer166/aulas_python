from log import LogFileMixin, LogPrintMixin


print('Salvando no main')

lp = LogPrintMixin()
lp.log_sucess("Passou")
lp.log_error('No passou')
    
lf = LogFileMixin()
lf.log_sucess('Passou no teste')
lf.log_error('Erro no teste')