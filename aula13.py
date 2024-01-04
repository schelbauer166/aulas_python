import enum

class Direcao(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    
    


def mover(direcao: Direcao):
    if not isinstance(direcao, Direcao):
        raise ValueError('Valor nao encontrado')
    
    
    
    print(f'Movendo para {direcao.name}')
    

mover(Direcao.ESQUERDA)