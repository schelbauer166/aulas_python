class Ponto:
    def __init__(self, x, y, z="String") -> None:
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self) -> str:
        name_ponto = f'{self.__class__.__name__}'
        return f'{name_ponto}({self.x!r}, {self.y!r}, {self.z!r})'
    

p1 = Ponto(1, 2)

print(p1)