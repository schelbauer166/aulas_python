from aula18_convert_size import convert_size
import os


caminho = os.listdir("/home/felipe/imagens")
caminho_2 = os.path.dirname('/home/felipe/imagens/')
contador = 1


for root, dirs, arquivos in os.walk(caminho_2):
    print(f'Pasta n: ', contador)
    contador += 1
    
    for arquivo in arquivos:
        print(arquivo, convert_size(os.path.getsize(arquivo)))






#for arquivos in caminho:
#    tamanho_arquivo = os.path.getsize(arquivos)
# #print(arquivos, convert_size(tamanho_arquivo))