from abc import ABC, abstractmethod


class FooAbrstract(ABC):
    
    def __init__(self, name): 
        self._name = name

    @property
    def name(self): 
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...
    
    

class Foo(FooAbrstract):

    
    
    @FooAbrstract.name.setter
    def name(self, name):
        self._name = name
        
        

l1 = Foo("Jorge")
l1.name = "Maria"


print(l1.name)