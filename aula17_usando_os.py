import os

print(os.system('clear'))

arquvo = os.path.join('/pasta1', 'arquivo.txt')

print(arquvo)

caminho = os.path.split(arquvo)
print(caminho)

novo = (os.path.splitext('arquivo.txt'))
print(novo)

print(os.path.basename(arquvo))
print(os.path.dirname(arquvo))



for root, dirs, files in os.walk('/home/felipe/teste'):
    print(root)
    
    for dir in dirs:
        print(dir)
    
    for file in files:
        print(file)
       