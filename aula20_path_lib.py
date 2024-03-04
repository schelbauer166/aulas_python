from pathlib import Path

caminho_file = Path().absolute()

#print(caminho_file)

caminho = Path(__file__).parent

#print(caminho)


novo_caminho = Path.home() / "texto.txt"


#novo_caminho.touch()
#novo_caminho.write_text("Hello world")
#novo_caminho.unlink()
print(novo_caminho)

with novo_caminho.open("+a") as file:
    file.write('Ol mundo \n')
    file.write("Ola mundos! \n")
    
    
    
print(novo_caminho.read_text())

novo_caminho.unlink()