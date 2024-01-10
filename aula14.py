import datetime
from dateutil.relativedelta import relativedelta




data = datetime.datetime(1989, 9, 27)
data_formt = data.strftime('%Y/%m/%d')

print(data_formt)

data_retro = datetime.datetime.now()

nova_data = data_retro - data
print(nova_data)

anos = datetime.timedelta(days= 12522)

anos_passados = relativedelta(datetime.datetime.now(), data)


print(anos_passados.years)


data = datetime.datetime.strptime('1989/09/27 21:30', '%Y/%m/%d %H:%M')
print(data)
nova_data = data.strftime('%d/%m/%Y %H:%M')
print(nova_data)