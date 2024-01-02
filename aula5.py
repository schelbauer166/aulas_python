class CarrinhoDeCompra:
    def __init__(self) :
        self.produtos = []
        
        
    def adicionar_produto(self, *produto):
        for p in produto:
            self.produtos.append(p)
        
    def valor_total(self):
        print()
        total = sum([p.preco for p in self.produtos])
        print(total)
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)
    
    
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
        
        
p1 = Produto("ameixa", 10 )
p2 = Produto("banana", 20 )
p3 = Produto("laranja", 5 )
carrinho = CarrinhoDeCompra()
carrinho.adicionar_produto(p1, p2, p3)
carrinho.listar_produtos()
carrinho.valor_total()