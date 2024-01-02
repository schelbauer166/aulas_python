import json


class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
        
dados = {'nome': 'Felipe',
         'idade': 34,
         'sexo': 'masculino'}

dados_2 = {'nome': 'Carol',
         'idade': 34,
         'sexo': 'feminino'}

#print(isinstance(dados, dict))

p1 = Pessoa(**dados)
p2 = Pessoa(**dados_2)

pessoas = [p1.__dict__, p2.__dict__]

def salvar(lista):
    with open('pessoas.json', 'w', encoding='utf8') as pessoaJson:
        json.dump(lista, pessoaJson, indent=2)
        
salvar(pessoas)