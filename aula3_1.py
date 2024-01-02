import json
from aula3 import Pessoa



try:
    with open('pessoas.json', 'r') as pessoasJson:
        pessoas = json.load(pessoasJson)
        p1 = Pessoa(**pessoas[0])
        p2 = Pessoa(**pessoas[1])
    
except FileNotFoundError:
        print("Arquivo nao localizado!")
        
        
print(p1.nome, p1.idade)
        
print(p2.nome, p2.idade)
