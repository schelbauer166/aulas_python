

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
        
    


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
        
    def escrever(self):
        print(f'{self.nome} esta escrevendo!')
        
        

escritor = Escritor('Felipe')
martelo = FerramentaDeEscrever('martelo')
caneta = FerramentaDeEscrever('Caneta Bic')



escritor.ferramenta = martelo

print(martelo.escrever())
print(escritor.ferramenta.escrever())

escritor.ferramenta = caneta
print(caneta.escrever())


print(escritor.ferramenta.escrever())