import json
import os

caminho_arquivo = os.path.abspath(os.path.join(os.path.dirname(__file__), 'filme_json'))

#print(caminho_arquivo)


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

string_dict = json.loads(string_json)
#print(string_json)
#print(string_dict)

with open(caminho_arquivo, "w") as arquivo:
    json.dump(string_dict, arquivo, ensure_ascii=False)
    
    