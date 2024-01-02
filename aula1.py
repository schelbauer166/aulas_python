import os, json


caminho_arquivo = '/home/felipe/project/'
caminho_arquivo += 'aula116.txt'


with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write("atenção\n")
    arquivo.write("Bom dia\n")
    arquivo.seek(0, 0)
    
    print(arquivo.readlines())
    
    
# os.unlink(caminho_arquivo)

os.rename(caminho_arquivo, "documento.txt")

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

#with open('pessoa.json', 'w') as arquivo:
#    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)


with open('pessoa.json', 'r') as arquivo:
    pessoa_1 = json.load(arquivo) 
    
print(pessoa_1)