import json









lista_de_tarefas = []
lista_de_tarefas_removidas = [] 


def salvar(lista):
    with open('tarefas.json', 'w', encoding='utf8') as tarefas_json:
        json.dump(lista, tarefas_json, indent=2)
        
        
def remover(lista):
    with open('tarefas.json', 'w', encoding='utf8') as tarefas_json:
        json.dump(lista, tarefas_json, indent=2)  
        
def listar():
    try:
        with open('tarefas.json', 'r') as tarefas_json:
            lista = json.load(tarefas_json)
            for i in lista:
                if i == '':
                    print('Lista vazia!')
                print(i, sep='\n')    
    except FileNotFoundError: 
        print("Lista Vazia")
        print()
        return
    
    

while True:
    
    print("Comandos: listar, desfazer, refazer")
    opcao = input("Digite uma tarefa ou comando: ")
    print()
   
    if opcao == 'listar':
        listar()
        
    elif opcao == 'desfazer':
        if lista_de_tarefas == []:
            print("Lista vazia!")
            continue
        excluida = lista_de_tarefas.pop()
        salvar(lista_de_tarefas)
        lista_de_tarefas_removidas.append(excluida)
        listar()
        print()
    elif opcao == 'refazer':
        retornada = lista_de_tarefas_removidas.pop()
        lista_de_tarefas.append(retornada)
        salvar(lista_de_tarefas)
        listar()
        print()
    else:
        lista_de_tarefas.append(opcao)
        salvar(lista_de_tarefas)