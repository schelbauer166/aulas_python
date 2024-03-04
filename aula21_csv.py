from pathlib import Path
import csv

caminho_csv = Path(__file__).parent / "aula21.csv"

print(caminho_csv)

with caminho_csv.open("r") as arquivo:
    #ele vai gerir uma [] com o reader, senao pode gerar um {} com o dictreader
    #leitor = csv.reader(arquivo)
    leitor_dict = csv.DictReader(arquivo)
    for linha in leitor_dict:
        print(linha)
        
    