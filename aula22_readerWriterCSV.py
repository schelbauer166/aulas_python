import csv
from pathlib import Path

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

caminho_csv = Path(__file__).parent / "aula22.csv"

with caminho_csv.open("w") as arquivo:
    leitor = csv.DictWriter(arquivo, fieldnames=lista_clientes[0])
    leitor.writeheader()
    
    for cliente in lista_clientes:
        leitor.writerow(cliente)
    
    
lista_clientes2 = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
 ]

with caminho_csv.open("+a") as arquivo:
    leitor = csv.writer(arquivo)
    colunas = ["Nome","Endereco"]
    leitor.writerow(colunas)
    
    for linha in lista_clientes2:
        leitor.writerow(linha)
            
    
    