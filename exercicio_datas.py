import datetime

from dateutil.relativedelta import relativedelta


valor_total = 1_000_000

data_inicial = datetime.datetime(year=2020, month=12, day=20)

data_final = data_inicial + relativedelta(years=+5)

print(data_final)

datas_ = []

while data_inicial < data_final:
    datas_.append(data_inicial)
    data_inicial += relativedelta(months=1)


numero_parcelas = len(datas_)
    
valor_parcela = valor_total / numero_parcelas
for data in datas_:
    print(data.strftime('%d/%m/%Y'), f'Valor parcela: {valor_parcela:,.2f}')
    

    