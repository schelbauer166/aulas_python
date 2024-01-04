def repr(self):
    name_= self.__class__.__name__
    dict_= self.__dict__
    class_repr = f'{name_}({dict_})'
    return class_repr


def meu_repr(cls):
    cls.__repr__ = repr
    return cls



def qual_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        print(resultado)
        if 'Terra' in resultado:
            return 'vc esta em casa'
        return resultado
    return interno


@meu_repr
class Planeta:
    def __init__(self, nome) -> None:
        self.nome = nome
        
    @qual_planeta    
    def meu_planeta(self):
        return f'Meu planeta e {self.nome}'
    
    
    
p1 = Planeta('Terra')

print(p1)